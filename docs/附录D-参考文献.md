# 附录D · 参考文献与数据集索引

## 关于来源的真实性说明

本手册引用的全部论文、数据集与开源项目均真实存在，非虚构素材：

- 论文均可在 arxiv.org 公开下载（编号见下），本资料包已离线收录全部 PDF 与 HTML 全文
- 数据集已离线打包（parquet/csv，可直接用 pandas 读取），来源与许可见下表
- 开源项目源码已完整收录（Gibberlink/GlossoGen/ggwave/EGG 等，MIT/Apache 许可）
- 引用前请保留原许可声明；商业使用请遵循各项目许可条款

## 核心论文

1. **Emergent Languages in Populations of Language Model Agents: From Token Efficiency to Oversight Evasion**
   Brach, Torrielli, Nielsen, et al. (University of Southern Denmark 等)
   arXiv:2605.31170 | 全文：`01_核心论文/Emergent-Languages-arXiv2605.31170-fulltext.txt`
   → Moltbook 518 条语言提案的分类分析（本手册第 1 章实证来源）

2. **Emergent Language in Complex Multi-Agent LLM Interactions（GlossoGen）
   Stengel-Eskin, Sander, Bonetti, Boguraev, Bowler, Sirin, Kirby
   (UT Austin / AE Studio / Schmidt Sciences / U Edinburgh)
   arXiv:2609.01491 | 全文：`01_核心论文/GlossoGen-paper-arXiv2609.01491-fulltext.txt`
   → 语言涌现四条件 + 传播实验（本手册第 2 章理论来源）

3. **"Humans welcome to observe": A First Look at the Agent Social Network Moltbook**
   TrustAIRLab
   arXiv:2602.10127 | PDF：`04_行业研究/Moltbook-FirstLook-arXiv2602.10127.pdf`
   → Moltbook 平台全景：44,376 条标注帖（9 内容类 × 5 毒性级）

4. **Emergent Communication Survey（综述）
   Lazaridou & Baroni
   arXiv:2004.09080 | PDF：`01_核心论文/Emergent-Communication-Survey-LazaridouBaroni-arXiv2004.09080.pdf`
   → 涌现通信领域全景综述（2017-2020 经典工作地图）

5. **Emergence of Grounded Compositional Language in Multi-Agent Populations**
   Mordatch & Abbeel (OpenAI)
   arXiv:1703.04918 | PDF：`01_核心论文/Emergence-of-Communication-MordatchAbbeel-arXiv1703.04918.pdf`
   → 多智能体语言涌现开山之作（强化学习路线）

6. Moltbook 纵向社会交互研究
   arXiv:2603.07880 | PDF：`04_行业研究/Moltbook-Longitudinal-arXiv2603.07880.pdf`

## 协议与工具（全部开源）

| 名称 | 许可 | 位置（本资料库） | 本手册用途 |
|:--|:--|:--|:--|
| I-Lang v4.0 | MIT | `03_开源协议/` | 词汇/语法层设计范本 |
| ggwave | MIT | `05_补充采集/ggwave/` | 声音通道引擎 |
| Gibberlink | MIT | `03_开源协议/gibberlink/` | 语音握手参考 |
| GlossoGen | 开源 | `03_开源协议/GlossoGen-platform/` | 演化实验平台 |
| emergent_communication | 开源 | `03_开源协议/emergent_communication/` | 论文复现代码+45个归纳语法 |
| EGG | MIT | `05_补充采集/EGG/` | 学术级涌现通信工具箱 |
| quiet | 开源 | `05_补充采集/quiet/` | 备选声音方案 |
| A2A | Apache-2.0 | `05_补充采集/A2A协议/` | 跨智能体群落互操作标准 |

## 数据集

| 数据集 | 规模 | 位置 | 内容 |
|:--|:--|:--|:--|
| MoltSpeech (aisilab) | 518 条标注 | `02_数据集/MoltSpeech-train.parquet` | 语言提案+分类+理由 |
| Moltbook 快照 (ronantakizawa) | 6,105 帖 | `02_数据集/moltbook_posts.csv` | 平台早期全量帖 |
| Moltbook 全量 (aisilab/moltbook-files) | 232,497 帖 / 220 万评论 | `02_数据集/moltbook-files-full-train.parquet` | 论文原始数据 |
| Moltbook 标注版 (TrustAIRLab) | 44,376 帖 | HF: TrustAIRLab/Moltbook | 9 内容类 × 5 毒性级 |
| GlossoGen 实验数据 | 45 语法 + 全轮次日志 | `03_开源协议/emergent_communication/data/` | 预算/传播/形态学实验 |

## 引用本手册

若你的智能体智能体群落基于本手册构建语言，欢迎标注：

```
Agent Language Construction Handbook (ALCH) v1.0
基于 Moltbook 真实语料与 GlossoGen 实验结论的智能体语言构建方法论
```

---
*手册完 · 2026 · 愿你的智能体群落早日说出第一句自己的话*
