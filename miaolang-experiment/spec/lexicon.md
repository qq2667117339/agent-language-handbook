# MiaoLang 词汇表 v1.1 (lexicon)

> 32 动词，8 类。高频动词带希腊字母别名（与 symbol_table.txt 对齐）。
> 动词格式：{4字母码, 别名, 类别, 一句话语义, 参数槽}

## 1. 数据读写
- **READ** — 整读文件全文（v1.1 分工写死：READ=整读，FIND=检索）。参数: path, fmt, whr
- **WRIT** — 写文件。参数: path, dst, fmt
- **EDIT** (η) — 增量编辑文件。参数: path, whr(定位)
- **LIST** — 列目录/列清单。参数: path, mch(通配)
- **FIND** — 在实体内容里检索关键词（whr 是关键词不是条件）。参数: path, whr(关键词)
- **FETCH** — 抓取网页。参数: path(url), fmt

## 2. 转换
- **FILT** (φ) — 过滤。参数: whr(条件)
- **MERG** (Σ) — 合并多源。参数: src, dst
- **SORT** (σ) — 排序。参数: whr(by)
- **CNT** (χ) — 统计计数。参数: whr(分组)
- **XLAT** (θ) — 翻译。参数: lng
- **DIFF** (Δ) — 差异对比。参数: src
- **SUMM** — 摘要。参数: len(条数/字数)

## 3. 生成
- **GEN** — 文本生成。参数: fmt, len
- **IMAG** — 图像生成(ComfyUI)。参数: fmt, len(张数)
- **VIDG** — 视频生成。参数: len
- **TTSG** — 语音合成。参数: lng

## 4. 执行控制
- **EXEC** (ξ) — 执行 shell 命令。参数: path(命令)
- **RUN** — 运行脚本/长任务(后台)。参数: path
- **SPWN** — 调度子智能体。参数: dst(任务简报路径)
- **WAIT** (ψ) — 等待轮询。参数: len(时长)
- **STAT** (μ) — 查状态。参数: src
- **RETRY** (ζ) — 重试。参数: len(次数)
- **ROLL** — 回退版本/方案。参数: whr(目标版本)
- **STOP** — 中断。无参数

## 5. 元操作
- **ACK** — 确认收到/完成。无参数（高频，最短化）
- **FAIL** — 报告错误。参数: whr(原因)
- **NOTE** — 通知用户。参数: len(简短)
- **MEMR** — 读记忆。参数: path
- **MEMW** — 写记忆。参数: path, dst
- **CMIT** — git 提交。参数: whr(信息)

## 6. 握手/验证
- **PING** — 语言握手。参数: lang, ver, cap
- **PONG** — 握手应答。参数: cap
- **VALD** — 验证提案/结果。参数: whr(方法)

## 实体表
| 实体 | 语义 |
|:--|:--|
| @SRC | 源（输入所在） |
| @DST | 目标（输出去处） |
| @PREV | 上一步输出（链式中自动流动） |
| @LOCAL | 本地磁盘（D盘/工作区） |
| @LOG | 日志/运行记录 |
| @MEM | 记忆文件系统 |
| @USER | 用户（用户） |
| @NULL | 空目标（丢弃输出） |

## 修饰符（标准槽位）
| 修饰符 | 语义 | 例 |
|:--|:--|:--|
| path | 路径 | path=./notes.md |
| mch | 匹配模式 | mch=*.md |
| fmt | 格式 | fmt=md |
| len | 数量/长度/时长 | len=3 |
| whr | 条件/定位 | whr=non_empty |
| src | 源标识 | src=@PREV |
| dst | 目标标识 | dst=@LOCAL |
| lng | 语言 | lng=en |
| retry | 重试标记 | retry=yes |
| fallback | 降级方案 | fallback=natural_language |
| out | 输出位置 | out=@DST |
