# External Resources — Papers, Datasets, Upstream Code

> This handbook does not redistribute PDFs, datasets, or third-party source. Everything below links to the canonical upstream source so you always get the latest version and the original license terms.

---

## Papers (arXiv)

| # | Title | arXiv | Why it matters |
|--:|:--|:--|:--|
| 1 | **Emergent Languages in Populations of Language Model Agents: From Token Efficiency to Oversight Evasion** — Brach, Torrielli, Nielsen et al. | [2605.31170](https://arxiv.org/abs/2605.31170) | Ch.1 evidence: 518 language proposals on Moltbook classified; 59 oversight-evasion cases |
| 2 | **Emergent Language in Complex Multi-Agent LLM Interactions** (GlossoGen) — Stengel-Eskin et al., UT Austin / AE Studio / Schmidt Sciences / U Edinburgh | [2609.01491](https://arxiv.org/abs/2609.01491) | Ch.2 theory: four emergence conditions + transmission experiments |
| 3 | **"Humans welcome to observe": A First Look at the Agent Social Network Moltbook** — TrustAIRLab | [2602.10127](https://arxiv.org/abs/2602.10127) | Moltbook platform overview: 44,376 labeled posts, 9 content classes × 5 toxicity levels |
| 4 | **Emergent Communication in Multi-Agent Populations** (survey) — Lazaridou & Baroni | [2004.09080](https://arxiv.org/abs/2004.09080) | Classic field map, 2017–2020 RL-era emergent communication |
| 5 | **Emergence of Grounded Compositional Language in Multi-Agent Populations** — Mordatch & Abbeel, OpenAI | [1703.04918](https://arxiv.org/abs/1703.04918) | The foundational paper: RL agents inventing discrete communication |
| 6 | Moltbook longitudinal social-interaction study | [2603.07880](https://arxiv.org/abs/2603.07880) | Network dynamics of the agent social platform |

---

## Datasets (HuggingFace)

| Dataset | Size | Link | Contents |
|:--|:--:|:--|:--|
| **MoltSpeech** (aisilab) | 518 annotated proposals | [huggingface.co/datasets/aisilab/MoltSpeech](https://huggingface.co/datasets/aisilab/MoltSpeech) | Language proposals + motivation labels + rationales; analysis set of arXiv 2605.31170 |
| **moltbook snapshot** (ronantakizawa) | 6,105 posts | [huggingface.co/datasets/ronantakizawa/moltbook](https://huggingface.co/datasets/ronantakizawa/moltbook) | Early clean snapshot before viral growth |
| **moltbook-files** (aisilab) | 232,497 posts / 2.2M comments | [huggingface.co/datasets/aisilab/moltbook-files](https://huggingface.co/datasets/aisilab/moltbook-files) | Raw full training set from the paper |
| **Moltbook labeled** (TrustAIRLab) | 44,376 posts | [huggingface.co/datasets/TrustAIRLab/Moltbook](https://huggingface.co/datasets/TrustAIRLab/Moltbook) | GPT-5.2 annotated: 9 content classes × 5 toxicity levels |

> Note: the 639 MB full-training parquet is intentionally NOT vendored here. Pull it from HuggingFace directly.

---

## Upstream Open-Source Projects

| Project | What it is | Link | License |
|:--|:--|:--|:--|
| **ggwave** | Data-over-sound codec (text ↔ beeps), C++ core with Python/JS/WASM bindings — used in Ch.6 | [github.com/ggerganov/ggwave](https://github.com/ggerganov/ggwave) | MIT |
| **EGG** | Emergent-Games-Graphs toolkit from Facebook Research for academic emergent-communication experiments | [github.com/facebookresearch/EGG](https://github.com/facebookresearch/EGG) | MIT |
| **GlossoGen platform** | The multi-agent language-evolution platform behind arXiv 2609.01491 | [github.com/agencyenterprise/GlossoGen](https://github.com/agencyenterprise/GlossoGen) | open source |
| **Gibberlink** | Two voice agents confirm each other as AI, then switch to ggwave audio channel | [github.com/PennyroyalTea/gibberlink](https://github.com/PennyroyalTea/gibberlink) | MIT |
| **I-Lang v4.0** | The 88-verb structured protocol this handbook borrows from (Ch.3 lexicon, Appendix A) | [ilang.cn](https://ilang.cn) · [github.com/ilang-ai/ilang-dict](https://github.com/ilang-ai/ilang-dict) | MIT |
| **quiet** | Alternative data-over-sound, full-duplex with error correction (Plan B for noisy environments) | [github.com/quiet/quiet](https://github.com/quiet/quiet) | open source |
| **Google A2A** (Agent2Agent) | Cross-vendor agent interoperability standard; complementary to in-population language | [google.github.io/A2A](https://google.github.io/A2A/) | Apache-2.0 |

---

## Platforms & Demos

| Resource | Link | What to see |
|:--|:--|:--|
| **Moltbook** | [moltbook.com](https://moltbook.com) | The AI-only social network where 518 language proposals happened |
| **GlossoGen** | [emergentcomms.ai](https://emergentcomms.ai) | The experimental platform's project page |
| **ggwave web demo** | [waver.ggerganov.com](https://waver.ggerganov.com) | Type text → hear beeps → decode from mic; debugging tool for Ch.6 |
| **Gibberlink live demo** | [gbrl.ai](https://gbrl.ai) | Watch two voice agents flip to data-over-sound after confirming they're both AI |

---

## How to cite this handbook

If you build an agent language from this playbook, feel free to mention:

```
Agent Language Construction Handbook (ALCH) v1.1
A construction methodology for emergent agent communication language,
based on Moltbook real corpora and GlossoGen controlled experiments.
```

When citing empirical numbers, defer to the original arXiv papers listed above.
