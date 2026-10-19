"""How far each RL round moves the policy, expert iteration vs GRPO (nd-rl long_rl_20261014, run v4:
untied model, two seeds per arm, 3 h RL budget). Three charts:

- kl-step: KL(new || old) between the policy before and after one round's update, on that round's
  rollouts. Per round, and GRPO runs ~5x more (shorter) rounds than EI in the same 3 h.
- kl-pretrained: KL(policy || pretrained) on the round's rollouts: total drift so far.
- nll-pretrain: the policy's -log p per token on 512 held-out pretraining records (forgetting).

All in nats per proof token, exact over the vocabulary at T = 1.
Data: rl_drift.csv, exported from nd-rl code/experiments/current/long_rl_20261014/report/data.json.
Run from the post dir:  python3 charts/rl_drift.py
"""
import csv

import altair as alt

from theme import HUE, save

WIDTH, HEIGHT = 560, 300
ARM = {"untied-ei": "Expert Iteration", "untied-grpo": "GRPO"}
COLOR = {"Expert Iteration": HUE["water"], "GRPO": HUE["carbon"]}

rows = [{"arm": ARM[r["arm"]], "seed": f"Seed {r['seed']}", **{k: float(r[k]) for k in r if k not in ("arm", "seed")}}
        for r in csv.DictReader(open("charts/rl_drift.csv"))]


def drift(col, name, title, y_title, log=False):
    chart = alt.Chart(alt.Data(values=rows)).mark_line(strokeWidth=1.8).encode(
        x=alt.X("clock:Q", title="RL Time (Hours)", scale=alt.Scale(domain=[0, 3]),
                axis=alt.Axis(values=[0, 0.5, 1, 1.5, 2, 2.5, 3])),
        y=alt.Y(f"{col}:Q", title=y_title, scale=alt.Scale(type="log") if log else alt.Scale(zero=True)),
        color=alt.Color("arm:N", title=None, scale=alt.Scale(domain=list(COLOR), range=list(COLOR.values())),
                        legend=alt.Legend(orient="bottom", direction="horizontal")),
        strokeDash=alt.StrokeDash("seed:N", title=None, scale=alt.Scale(range=[[1, 0], [5, 4]]), legend=None),
        detail="seed:N",
    ).properties(width=WIDTH, height=HEIGHT, title=title)
    save(chart, name, WIDTH)


drift("kl_step", "kl-step", "KL to Previous Round", "KL per Token (Nats, Log Scale)", log=True)
drift("kl_pre_roll", "kl-pretrained", "KL to Pretrained, on Rollouts", "KL per Token (Nats)")
drift("nll_pt", "nll-pretrain", "Loss on Held-Out Pretraining Proofs", "−log p per Token (Nats)")
