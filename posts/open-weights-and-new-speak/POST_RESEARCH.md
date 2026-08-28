# Research: "open source" vs "open weights" controversies

For footnote `[^cv]`. Each entry: what happened, why it matters for the "word survives, substance
drifts" thesis. Dates are release/publication years.

## Definitions in play

- **OSI Open Source Definition** (1998): the traditional bar. Free redistribution, source included,
  no discrimination against persons/groups or fields of endeavor. Llama, Gemma, RAIL-licensed models
  fail the "no discrimination" clauses outright.
- **OSI Open Source AI Definition, OSAID 1.0** (Oct 2024): OSI's attempt to say what "open source
  AI" requires: weights + training/inference code + "sufficiently detailed information about the
  data" to let a skilled person rebuild a substantially equivalent system. Does _not_ require
  releasing the data itself. https://opensource.org/ai/open-source-ai-definition
- **"Open-weight"** as a term emerged ~2023 as a retreat term once "open source" started getting
  policed; it promises only the parameters. This is the first lexical drift, the one the post builds
  on.

## Controversies

### 1. Llama license (2023–2024): "open source" per Meta, not per anyone else

- Llama 2 (2023) and Llama 3 (2024) ship under the "Llama Community License". Key clauses: (a) any
  product with >700M monthly active users needs a separate license from Meta, i.e. explicitly
  excludes competitors; (b) an Acceptable Use Policy listing banned uses; (c) until 3.1 (2024), you
  couldn't use Llama outputs to train non-Llama models.
- Meta's marketing consistently said "open source" (Zuckerberg's July 2024 letter "Open Source AI Is
  the Path Forward").
- OSI's executive director Stefano Maffulli publicly said Llama is not open source (Financial Times,
  Oct 2024). Meta's reply, paraphrased: the OSI definition doesn't fit AI, we'll keep using the
  term.
- Llama 3.2's multimodal models (2024) are not licensed for use in the EU at all: a geographic gate,
  the closest existing analogue to the post's "permit" bullet.
- Sources: https://ai.meta.com/llama/license/ ;
  https://about.fb.com/news/2024/07/open-source-ai-is-the-path-forward/ ; FT "Meta under fire for
  'polluting' open-source" (2024).

### 2. OSAID backlash (2024): the definition exists, nobody's flagship meets it, word survives

- Purists (e.g. Software Freedom Conservancy, some Debian people) argued OSAID is too lax because it
  doesn't require the training data, so "open source AI" would not be reproducible in the way open
  source software is.
- Labs argued it was too strict, because data can't be released for copyright/privacy reasons.
- Net result: as of 2025, the models that qualify are mostly research artifacts (OLMo from AI2,
  Pythia from EleutherAI, BLOOM's successors). Llama, Gemma, Mistral's non-Apache models, and Qwen
  (which is Apache-2.0 on weights but releases no data) don't. Everyone kept using the words.
- Source: https://opensource.org/ai ; Liesenfeld & Dingemanse, "Rethinking open source generative
  AI: open-washing and the EU AI Act" (FAccT 2024), which ranks ~40 "open" models on 14 openness
  dimensions and coins/popularizes "open-washing" for this space.
  https://dl.acm.org/doi/10.1145/3630106.3659005

### 3. EU AI Act (2024): a legal reason to be called open

- The Act gives general-purpose models released under "free and open-source licenses" lighter
  obligations (transparency exemptions), _unless_ they're classified as systemic-risk models.
- This creates a direct incentive to open-wash: the label buys regulatory relief. Liesenfeld &
  Dingemanse's paper is explicitly about this loophole.
- Relevant to the post: this is the first time a government has attached legal consequences to the
  word, which is the mechanism by which the word gets fought over and hollowed out.

### 4. RAIL / OpenRAIL licenses (2022): "open" with a behavioral leash

- BLOOM (BigScience, 2022) and Stable Diffusion (2022) shipped under Responsible AI Licenses:
  weights downloadable, but a list of prohibited uses (medical advice, generating disinformation,
  etc.).
- OSI position: use restrictions violate "no discrimination against fields of endeavor", so not open
  source. The RAIL authors' position: that's the point.
- Established the norm that a downloadable model can carry a use policy, which later licenses (Llama
  AUP, Gemma prohibited-use policy) copied.
- Source: https://www.licenses.ai/

### 5. Gemma terms (2024): open, plus a remote kill clause

- Google released Gemma as "open" and carefully _not_ "open source". Terms of Use include a
  prohibited-use policy and reserve Google's right to update terms and restrict usage after the
  fact.
- Google's own blog explained the word choice, which is a rare case of a lab being precise about the
  distinction.
- Source: https://ai.google.dev/gemma/terms

### 6. Tiered-by-strength licensing: Mistral and Stability (2023–2024)

- Mistral: Mistral 7B and Mixtral 8x7B are Apache-2.0. The stronger models (Codestral, Mistral Large
  weights, Pixtral Large) ship under the "Mistral Research License" / "Mistral AI Non-Production
  License": non-commercial only. Same lab, same word "open", the gate tightens with capability.
- Stability AI "Community License" (2024): free under $1M annual revenue, paid above. Tiered by
  revenue rather than by permit, but structurally a permit scheme.
- Directly supports the post's trajectory: the stronger the model, the narrower the "open".

### 7. The genuinely open counterexamples come from China (2024–2025)

- Qwen (Alibaba) and DeepSeek release most weights under Apache-2.0 / MIT with no use policy and no
  MAU cap. These are the models that actually meet the plain meaning of "open-weight".
- Political relevance for the post: the most-open frontier-adjacent models are from the US's main
  strategic competitor, which is a big part of why the US government has an interest in redefining
  the term rather than just endorsing it.

## One-line summary for the footnote

"Open source" for AI has already been redefined twice: once when labs (Meta, Google) applied it to
models with use restrictions and competitor carve-outs, prompting OSI to publish a definition (2024)
that almost no flagship model meets; and once when "open-weight" was coined as a retreat term. The
EU AI Act (2024) then attached regulatory relief to the label, giving everyone a reason to keep the
word.
