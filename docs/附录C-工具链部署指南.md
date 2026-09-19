# 附录C · 工具链部署指南

> 语言工程的三类工具：研究工具（EGG/GlossoGen）、协议参照（I-Lang）、声音通道（ggwave/Gibberlink）。
> 本资料库 `05_补充采集/` 与 `03_开源协议/` 已含全部源码，离线可部署。

## C-1 ggwave（声音通道引擎）

- 位置：`05_补充采集/ggwave/`（含官方 Python 绑定 `bindings/python`）
- 部署：
  ```bash
  cd ggwave/bindings/python
  pip install .        # 需 Cython + C++ 编译环境（MSVC/gcc）
  python test.py       # 自带测试
  ```
- 依赖：pyaudio（录音播放）、numpy
- 坑位：Windows 编译需 VS Build Tools；Linux 需 `apt install portaudio19-dev`
- 用途：第 6 章语音协议全部实现

## C-2 Gibberlink（声音握手参考实现）

- 位置：`03_开源协议/gibberlink/gibberlink-main/`
- 内容：Next.js demo（两个语音智能体确认彼此后切 ggwave）+ wiki 里的复现步骤
- 用途：第 6.4 节语音握手的工程参照；Web demo 可开 gbrl.ai 直接体验

## C-3 EGG（涌现通信研究工具箱）

- 位置：`05_补充采集/EGG/`（Facebook Research）
- 部署：
  ```bash
  cd EGG
  pip install -e .
  ```
- 用途：学术级涌现通信实验（referential games、语言漂移分析）。做严肃研究用，快速验证用 GlossoGen 更轻
- 文档：仓库内 docs/ 有完整教程

## C-4 GlossoGen 平台（多智能体语言演化实验）

- 位置：`03_开源协议/GlossoGen-platform/`（平台）+ `03_开源协议/emergent_communication/`（论文代码+实验数据）
- 用途：复现第 2 章实验（预算压力/postmortem/传播）；`emergent_communication/data/` 里有 45 个已归纳语法（`data/mdl/grammars/`），可直接拿来当语言设计参考
- 论文代码注意：部分脚本需 LLM API（评测用），数据文件离线可用

## C-5 I-Lang（协议参照）

- 位置：`03_开源协议/I-Lang-v4.0-官网全文-ilang.cn.txt` + `ilang-v4.0-protocol-header.txt`
- 部署：零安装。协议头直接粘进任何 LLM 对话即激活
- 用途：第 3 章词汇/语法层的设计范本；88 动词表直接借用（附录A）
- 协议头实测：ChatGPT/Claude/Gemini/DeepSeek/Kimi/豆包均通过

## C-6 MoltSpeech 数据集（真实语料）

- 位置：`02_数据集/MoltSpeech-train.parquet`（518 条标注）+ `moltbook_posts.csv`（6105 帖全量快照）
- 读取：
  ```python
  import pandas as pd
  df = pd.read_parquet("MoltSpeech-train.parquet")
  df['reason'].value_counts()   # token_efficiency 166 / spoken 106 / ...
  ```
- 用途：第 1 章实证；为自己的语言设计找真实参照（每条提案含完整 rationale）

## C-7 quiet（备选声音方案）

- 位置：`05_补充采集/quiet/`
- 定位：调制解调式数据-over-声音，比 ggwave 复杂（全双工、纠错更强），速率更低
- 何时用：ggwave 在极端噪声环境失败率不可接受时，作为 Plan B

## C-8 A2A 协议（智能体互操作标准）

- 位置：`05_补充采集/A2A协议/`
- 定位：Google 的 Agent2Agent 标准——解决的是"不同厂商智能体如何互操作"，与本手册"智能体群落内部语言"互补
- 何时用：自研框架需要对外暴露标准接口时参考；智能体群落内部通信用本手册语言，跨智能体群落通信走 A2A

---
*附录D → 参考文献*
