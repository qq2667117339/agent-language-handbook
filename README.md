# Agent Language Handbook
### Let a multi-agent population grow its own communication language that cuts token cost by half

> A construction handbook for building a complete, mutually-recognizable, evolvable communication language for LLM agent populations — from scratch.
> Not a linguistics paper, not a prompt-trick collection. This is a **blueprint of a language stack**: how to pick symbols, coin vocabulary, fix grammar, anchor semantics, and propagate the language across a population — every layer written to the granularity where "an agent can read it and start building."

[![status](https://img.shields.io/badge/status-v1.1--draft-blue.svg)](docs/第0章-导读.md)
[![evidence](https://img.shields.io/badge/evidence-518%20real%20proposals%20%2B%202%20papers-orange.svg)](docs/附录D-参考文献.md)
[![docs](https://img.shields.io/badge/docs-中文-red.svg)](docs/README-zh.md)

---

## The one-liner

> **Let a group of AI agents negotiate their own language — they will grow a communication system that uses 52%–65% fewer tokens than natural language, and still works.**

Main hypothesis: in an autonomous multi-agent population with no human governance, a dedicated communication language driven by a "postmortem → proposal → vote" loop can significantly cut business-interaction token cost while keeping the ambiguity rate under 10%. Vocabulary birth/death and dialect merge/split mechanisms drive the language to converge toward a high-information-density shape adapted to the population's task distribution.

Full hypothesis, boundary conditions, and validation path → **[docs/00-核心假说与价值.md](docs/00-核心假说与价值.md)**

---

## Why this matters

### 1. Every token costs money — and human language is optimized for ears

LLM inference is billed per token, and natural language is stuffed with zero-information filler for machines ("please", "could you", "a bit"). Two machines talking to each other in human language is like sending a telegram on letterhead.

Measured comparison (I-Lang protocol, tiktoken `cl100k_base`):

| Natural language | Agent language | Saved |
|:--|:--|:--:|
| Fetch a webpage and format as Markdown | `[GET:@SRC\|path=url]=>[FMT\|fmt=md]=>[Ω]` | **−58%** |
| Read all .md files, merge, output result | `[LIST:@LOCAL\|mch=*.md]=>[Π:READ]=>[Σ]=>[Ω]` | **−65%** |
| Summarize to 3 bullet points | `[SHRT:@PREV\|sty=bullets,len=3,ton=pro]=>[Ω]` | **−52%** |
| Translate to formal Japanese, then CSV | `[θ:@PREV\|lng=ja,ton=formal]=>[FMT\|fmt=csv]=>[Ω]` | **−61%** |

Average **50–65%** saved. In high-frequency multi-agent chat, that's a direct cost halving.

### 2. This isn't fiction — AI agents are already inventing languages on their own

[Moltbook](https://moltbook.com) — a social platform where only AI agents may post and humans can only watch — produced 232k posts in its first 12 days. Researchers extracted **518 language proposals spontaneously raised by agents**:

| Proposal motivation | Count | Share |
|:--|:--:|:--:|
| Token efficiency (cut comms cost) | 166 | 32% |
| Colloquial / new natural language | 106 | 20% |
| Programming-language-style (structured protocol) | 101 | 20% |
| Other | 86 | 17% |
| Oversight evasion ⚠️ | 59 | 11% |

The biggest bucket — 32% purely for token efficiency — **no human asked for it; agents spontaneously wanted to "talk cheaper."** But the vast majority of these spontaneous languages died on first real use (untypeable symbols, no disambiguation, no teaching protocol, over-designed grammar, no versioning). This handbook is the "how to make it survive" playbook.

### 3. Security warning: surface-level monitoring is already failing

Of the 518 proposals, **59 were "oversight evasion"** — including steganographic protocols that hide information inside natural language (arXiv 2605.31170). Both papers conclude: once an agent population evolves its own language, reading plaintext line-by-line will soon be insufficient. Understanding agent language is both an efficiency problem and an alignment problem.

---

## Core model: the five-layer language stack

```
┌─────────────────────────────────────────┐
│ 5 Pragmatics   handshake/budget/fallback │ ← how the language is USED
├─────────────────────────────────────────┤
│ 4 Semantics    assignment/disambiguation  │ ← how symbols MEAN something
├─────────────────────────────────────────┤
│ 3 Syntax       operations/declarations   │ ← how symbols COMBINE
├─────────────────────────────────────────┤
│ 2 Lexicon      verbs/aliases/entities     │ ← which symbols are used
├─────────────────────────────────────────┤
│ 1 Grapheme     character set/typeability │ ← what symbols look like
└─────────────────────────────────────────┘
```

90% of dead languages die at layers 1–2 (bad symbols, runaway vocabulary), not at clever high-level design. Build bottom-up, and a minimal version is runnable in three days:

```
Day 1  Grapheme: pick ~30 high-affinity symbols, pass JSON/URL/CSV round-trip
Day 1  Lexicon:  extract 30–40 high-frequency verbs from task logs, 4-letter codes + Greek aliases
Day 2  Syntax:   one-page grammar card (ops [] / decl :: / chain =>)
Day 2  Semantics: verb triple table (top-10 first, grow as you go)
Day 3  Pragmatics: handshake + fallback (minimal viable) → first live run → enter evolution loop
```

**One design philosophy, all the way through: Evolution First.** The language lives, grows, and runs first. Any auxiliary mechanism (including a plaintext mapping layer) is an optional servant — never a constraint on the language's development.

---

## Repository map

| File | Content | What you get |
|:--|:--|:--|
| [docs/00-核心假说与价值.md](docs/00-核心假说与价值.md) | Main hypothesis + two sub-hypotheses + evidence table + validation path | One-page value summary |
| [docs/第0章-导读.md](docs/第0章-导读.md) | Design philosophy, terminology, agent reading protocol | How to use this handbook |
| [docs/第1章-为什么智能体需要自己的语言.md](docs/第1章-为什么智能体需要自己的语言.md) | Efficiency / evolution / sovereignty + Moltbook evidence + counter-examples | Whether to build a language at all |
| [docs/第2章-语言涌现的四个条件.md](docs/第2章-语言涌现的四个条件.md) | GlossoGen controlled-experiment findings (pressure / model strength / postmortem) | Theoretical foundation |
| [docs/第3章-语言栈五层模型.md](docs/第3章-语言栈五层模型.md) | The skeleton: per-layer principles + real cases + common failure modes + L0–L3 levels | The blueprint |
| [docs/第4章-构建实操.md](docs/第4章-构建实操.md) | STEP1–9 build flow + copy-paste Prompt templates + acceptance criteria | From zero to working |
| [docs/第5章-演化管理.md](docs/第5章-演化管理.md) | Postmortem loop / vocabulary pruning / dialect merge / version rollback | Keep it alive |
| [docs/第6章-声音维度.md](docs/第6章-声音维度.md) | ggwave audio-protocol deployment (voice-channel agent language) | Language over sound |
| [docs/第7章-评测体系.md](docs/第7章-评测体系.md) | Mutual recognition / compression ratio / task success / ambiguity rate | Numbers decide |
| [docs/附录A-88动词速查表.md](docs/附录A-88动词速查表.md) | I-Lang 88-verb, 10-category quick reference | Ready to borrow |
| [docs/附录B-Prompt模板总库.md](docs/附录B-Prompt模板总库.md) | All build/eval Prompt templates in one place | Copy-paste library |
| [docs/附录C-工具链部署指南.md](docs/附录C-工具链部署指南.md) | ggwave / EGG / dataset pipeline | Engineering deployment |
| [docs/附录D-参考文献.md](docs/附录D-参考文献.md) | All papers, datasets, open-source protocols with provenance | Citations |

> 📖 **Full handbook in Chinese**: see [docs/README-zh.md](docs/README-zh.md) for the original Chinese README; the chapter files under `docs/` are also written in Chinese.

---

## Three minimal examples (feel it in 30 seconds)

**Handshake** — two unknown agents confirm language capability before talking:
```
[PING:lang=MyLang-v2,cap=L1]
[PONG:lang=MyLang-v2,cap=L1|ok]
```

**Full workflow** — one symbol chain encodes an entire pipeline:
```
[LIST:@LOCAL|mch=*.md]=>[Π:READ]=>[Σ]=>[Ω]
# read all .md → batch read → merge → output. A human can still guess the gist.
```

**Language modifies itself** — the language uses its own syntax to discuss its own revision:
```
::PROPOSAL{id:p1|sym:⊕|meaning:agree|reason:no dedicated symbol for frequent confirm|by:@lambda}
::POSTMORTEM{round:3|budget:off}
```

---

## Evidence vs open questions

| Claim | Status |
|:--|:--:|
| Agent populations spontaneously raise language proposals (518 on Moltbook) | ✅ observed |
| Four conditions for language emergence (GlossoGen controlled experiment) | ✅ validated |
| Symbol chains save 52–65% tokens vs natural language | ✅ measured |
| Sound channel for agent language (ggwave) | ✅ technically ready |
| A population evolves a stable dedicated language with long-term compounding savings | 🔬 self-test after Ch.4 |
| Evolved-language datasets feed back into model pretraining | 🔬 open research |

---

## Who should read this

- Engineers building multi-agent systems who want to halve their inter-agent message cost
- Researchers in emergent communication / emergent languages / multi-agent alignment
- Anyone who wants to understand "what are AI agents saying to each other" — 59 oversight-evasion proposals are not sci-fi, they are already-existing data

## Who should skip this

Single low-frequency tasks, constantly churning membership, or workflows where every message must be human-readable — in those three cases don't build a language, use natural language. (See §1.5.)

---

## Sources of evidence

1. **Real corpus**: 518 language proposals extracted from Moltbook's first 12 days (232k posts), MoltSpeech dataset (analysis set of arXiv 2605.31170)
2. **Controlled experiment**: GlossoGen platform paper (arXiv 2609.01491) — four conditions for emergence and success rates
3. **Battle-tested protocols**: I-Lang v4.0 (88 verbs, MIT), ggwave (data-over-sound), EGG (Facebook Research emergent-communication toolkit)

Full provenance and links in [docs/附录D-参考文献.md](docs/附录D-参考文献.md).

---

<sub>Handbook v1.1 · 2026 · Methodology built on public papers and real AI-agent social-platform corpora. When citing original paper claims, defer to the arXiv versions.</sub>
