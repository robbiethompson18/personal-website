"""Pull the Stage-1 numbers out of ../nd-takehome into CSVs next to the charts.

The eval outputs it reads live in /tmp and get cleared; the CSVs it writes are committed, so the
chart scripts stay runnable afterwards.  Re-run this only when the models are retrained.

    cd posts/natural-deduction-takehome && python3 charts/extract.py

Writes charts/loss_curves.csv, charts/solve_by_length.csv, charts/written_length.csv.
"""
import collections
import csv
import json
import os
import subprocess
import sys

ND = os.path.expanduser("~/repos/nd-takehome")
POS = ("nope", "rope")


def out(name, fields, rows):
    with open(f"charts/{name}.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    print(f"wrote charts/{name}.csv ({len(rows)} rows)")


def loss_curves():
    """Train / held-out loss per logged step, straight out of the checkpoints."""
    import torch
    rows = []
    for pos in POS:
        ck = torch.load(f"{ND}/ckpts/stage1_{pos}.pt", map_location="cpu", weights_only=False)
        for h in ck["extra"]["history"]:
            if "train_loss" in h:                       # the other entries are greedy evals
                rows.append({"pos": pos, "step": h["step"], "epoch": round(h["epoch"], 2),
                             "train_loss": h["train_loss"], "val_loss": h["val_loss"]})
    out("loss_curves", ["pos", "step", "epoch", "train_loss", "val_loss"], rows)


def scored(path, verify_text):
    for line in open(path):
        r = json.loads(line)
        ok, _, n_lines = verify_text(r["prompt"] + " " + r["proof"])
        yield r, ok, n_lines


def solve_and_written():
    """Solve rate by the length of the proof the theorem was generated with, and the histogram of
    lengths the model actually wrote on the >6 pools.

    Lengths 2-6 come from the checkpoint's own recorded final eval rather than from a re-scored
    file: data/heldout.jsonl keeps growing as new theorem classes are appended, so re-scoring it
    later would silently measure a different set than the one these models were evaluated on."""
    import torch
    sys.path.insert(0, ND)
    from nd_verify import verify_text
    from nd_verify.verify import parse_proof_tokens

    long_ref = {}
    for pool in ("rl_targets", "transfer"):
        for l in open(f"{ND}/data/long/{pool}.jsonl"):
            r = json.loads(l)
            long_ref[r["prompt"]] = r["gen_lines"]

    solve = collections.Counter()      # (pos, gen_len) -> [solved, n]
    n = collections.Counter()
    written = collections.Counter()    # (pos, written_len, verified) -> count
    invalid = collections.Counter()
    for pos in POS:
        ck = torch.load(f"{ND}/ckpts/stage1_{pos}.pt", map_location="cpu", weights_only=False)
        for L, (k, m, _ci) in ck["extra"]["final"]["by_len"].items():
            solve[(pos, L)] += k
            n[(pos, L)] += m
        for pool in ("rl_targets", "transfer"):
            for r, ok, _ in scored(f"/tmp/long_{pos}_{pool}.jsonl", verify_text):
                gen_len = long_ref[r["prompt"]]
                try:
                    w = len(parse_proof_tokens(r["proof"].split()))
                    written[(pos, w, ok)] += 1
                except Exception:
                    w, _unused = None, invalid.update([pos])
                # A solve is filed under min(generating length, length written): finding a 5-line
                # proof for a theorem the generator built in 14 is evidence the theorem is a
                # 5-liner, not that the model proved a 14-liner.  Note this tightens the numerator
                # only -- an unsolved target has no known shortest proof, so it stays at gen_len.
                # Robbie is writing the caveat that goes with this in the post.
                L = min(gen_len, w) if (ok and w) else gen_len
                n[(pos, L)] += 1
                solve[(pos, L)] += ok

    out("solve_by_length", ["pos", "gen_lines", "solved", "n"],
        [{"pos": p, "gen_lines": L, "solved": solve[(p, L)], "n": n[(p, L)]}
         for (p, L) in sorted(n)])
    out("written_length", ["pos", "written", "verified", "count"],
        [{"pos": p, "written": w, "verified": int(v), "count": c}
         for (p, w, v), c in sorted(written.items())])
    print(f"unparseable model outputs, excluded from written_length: {dict(invalid)}")


def rule_use():
    """Share of training proofs that use each rule at least once."""
    n, uses = 0, collections.Counter()
    for line in open(f"{ND}/data/train.jsonl"):
        r = json.loads(line)
        n += 1
        for rule in set(r["rules"]):
            uses[rule] += 1
    out("rule_use", ["rule", "proofs", "total"],
        [{"rule": k, "proofs": v, "total": n} for k, v in uses.most_common()])


def solve_curve():
    """Greedy held-out solve rate at each mid-training eval."""
    import torch
    rows = []
    for pos in POS:
        ck = torch.load(f"{ND}/ckpts/stage1_{pos}.pt", map_location="cpu", weights_only=False)
        n_train = 142118                       # the split these two runs trained on
        for h in ck["extra"]["history"]:
            if "rate" in h:
                rows.append({"pos": pos, "step": h["step"],
                             "epoch": round(h["step"] * 1024 / n_train, 2),
                             "solved": h["solved"], "n": h["n"], "rate": h["rate"]})
    out("solve_curve", ["pos", "step", "epoch", "solved", "n", "rate"], rows)


def error_breakdown():
    """Why the verifier rejected the model's attempt on the >6 pools."""
    sys.path.insert(0, ND)
    from nd_verify import verify_text
    rows = collections.Counter()
    for pos in POS:
        for pool in ("rl_targets", "transfer"):
            for r, ok, _ in scored(f"/tmp/long_{pos}_{pool}.jsonl", verify_text):
                if not ok:
                    reason = r_short(r, verify_text)
                    rows[(pos, reason)] += 1
    out("error_breakdown", ["pos", "reason", "count"],
        [{"pos": p, "reason": s, "count": c} for (p, s), c in rows.most_common()])


def r_short(r, verify_text):
    """Collapse the verifier's diagnostic to its family (it appends line numbers / rule names)."""
    reason = verify_text(r["prompt"] + " " + r["proof"])[1]
    reason = reason.split("(")[0].strip()
    if reason.startswith("parse:"):
        return "parse error"
    if reason.startswith("rule check failed"):
        return "rule check failed"
    return reason


if __name__ == "__main__":
    loss_curves()
    solve_and_written()
    rule_use()
    solve_curve()
    error_breakdown()


def solved_lengths():
    """For every solved target in the >6 pools: the length it was generated with vs the length the
    model actually wrote.  This is what shows the pool's difficulty labels are inflated."""
    sys.path.insert(0, ND)
    from nd_verify import verify_text
    from nd_verify.verify import parse_proof_tokens
    ref = {}
    for pool in ("rl_targets", "transfer"):
        for l in open(f"{ND}/data/long/{pool}.jsonl"):
            r = json.loads(l)
            ref[r["prompt"]] = r["gen_lines"]
    pairs = collections.Counter()
    for pos in POS:
        for pool in ("rl_targets", "transfer"):
            for r, ok, _ in scored(f"/tmp/long_{pos}_{pool}.jsonl", verify_text):
                if ok:
                    pairs[(ref[r["prompt"]], len(parse_proof_tokens(r["proof"].split())))] += 1
    out("solved_lengths", ["gen_lines", "written", "count"],
        [{"gen_lines": g, "written": w, "count": c} for (g, w), c in sorted(pairs.items())])
