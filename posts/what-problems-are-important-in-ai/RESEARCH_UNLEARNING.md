# State of unlearning and data filtering (Aug 2026)

Research note for the Safeguards section. Three families of technique, in rough order of how well
they actually hold up.

## 1. Post-training unlearning (fine-tune the knowledge out)

- **WMDP / RMU** — Li et al. (2024), https://arxiv.org/abs/2403.03218. The standard benchmark: 3,668
  MCQs proxying bio/cyber/chem hazard knowledge. RMU ("representation misdirection") pushes
  hazardous-input activations toward random vectors; drops WMDP accuracy to near chance with small
  MMLU cost. This is the method everyone compares against.
- **It's mostly suppression, not removal.** Deeb & Roger (2024), https://arxiv.org/abs/2410.08827:
  fine-tuning on a handful of _unrelated_ facts from the same distribution recovers ~88% of
  pre-unlearning accuracy. Łucki et al. (2024), https://arxiv.org/abs/2409.18025: RMU broken by
  fine-tuning, orthogonalization, and pruning; the knowledge is still in the weights.
- **Tamper-resistant variants** (TAR, Tamirisa et al., ICLR 2025, https://arxiv.org/abs/2408.00761)
  meta-learn against relearning attacks. They help but trade off capability/stability, and later
  attacks with more fine-tuning steps still recover most of it.
- **Model-tampering evals** (Che et al., 2025, https://arxiv.org/abs/2502.05209) are now the
  accepted bar: an unlearning claim is only meaningful if it survives an attacker with weights +
  fine-tuning budget. Open problems survey: Barez et al. (2025), https://arxiv.org/abs/2501.04952.

Bottom line: post-training unlearning is adequate against API users (who can't fine-tune) and
inadequate for open weights.

## 2. Localize-then-delete (route the knowledge to a part you can cut out)

- **Gradient routing** — Cloud et al. (2024), https://arxiv.org/abs/2410.04332. Mask gradients so
  forget-set data only updates a designated sub-region; ablate that region at the end. Demonstrated
  on a 28M-param toy LM; works better than RMU on that scale, unclear at frontier scale. This is the
  "route to one expert and delete it" idea.
- **Distillation robustifies unlearning** — Lee et al. (2025), https://arxiv.org/abs/2506.06278.
  Unlearn with a suppression method, then distill into a fresh student: the student never sees the
  suppressed knowledge, so relearning attacks fail. Costs a full distillation run.

## 3. Pretraining data filtering (never teach it)

- **Anthropic** (2025), https://alignment.anthropic.com/2025/pretraining-data-filtering/. Classifier
  over pretraining corpus (synthetic labels from WMDP-style Q&A); filtering cut CBRN-eval
  performance ~33% at the chosen threshold with no benchmark degradation.
- **Deep Ignorance** — O'Brien et al. (EleutherAI / UK AISI / OATML, 2025),
  https://arxiv.org/abs/2508.06601. 6.9B models pretrained from scratch on bio-filtered data resist
  adversarial fine-tuning of up to 10k steps / 300M tokens of biothreat text — >10× more
  tamper-resistant than RMU/TAR baselines, no capability hit. Caveat: the model can still _use_ the
  knowledge if handed it in context (search, RAG), so filtering is not sufficient alone.
- Follow-up: token-level filtering (2026), https://arxiv.org/abs/2601.21571.

Bottom line: filtering is the only technique with strong evidence of tamper resistance, and it's the
one you can't apply retroactively — it has to be done before the pretraining run. It's also the only
one that's viable for open-weight releases.

## Takeaway for the post

"Unlearning" is the term of art for (1); "data filtering" for (3); (2) sits between. Against API
access all three plus classifiers work. Against open weights, only (3) (and maybe distillation)
survives, and even then in-context provision of the knowledge defeats it.
