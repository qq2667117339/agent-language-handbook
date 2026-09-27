# MiaoLang 互测 — GLM-5.3 Flash（零先验解析）

> 依据：仅 grammar_card.md v0.1 + lexicon.md v0.1。未使用任何外部先验。

## 动词释义（5条）

1. **READ** — 读取文件内容（参数槽：path 路径 / fmt 格式 / whr 条件定位）。
2. **MERG**（别名 Σ）— 把多个来源的内容合并为一个输出（参数槽：src 源标识 / dst 目标标识）。
3. **FAIL** — 报告错误/失败状态，必须给出原因（参数槽：whr=原因），规范禁止失败时沉默。
4. **SPWN** — 调度派生一个子智能体去执行任务（参数槽：dst=任务简报路径）。
5. **SUMM** — 对内容做摘要压缩（参数槽：len=条数/字数）。

## 指令改写（5条）

### 1. 读取 data 目录下所有 csv，合并成一个文件

```
[LIST:@SRC|path=./data,mch=*.csv]=>[READ:@PREV]=>[MERG|dst=./merged.csv]=>[Ω]
```

（仿语法卡示例 `[LIST:@SRC|mch=*.md]=>[Σ]=>...` 的链式流；MERG 输出写入 dst 文件后经 Ω 输出。）

### 2. 把上一条结果翻译成英文，摘要成3点

```
[XLAT:@PREV|lng=en]=>[SUMM|len=3]=>[Ω]
```

（θ=XLAT 带 lng=en；SUMM len=3 即摘要成3条；@PREV 承接上一步输出。）

### 3. 检查日志里有没有报错，有就通知我

```
[READ:@LOG|whr=error]=>[φ:non_empty]=>[NOTE:@USER|len=short]
```

（读日志、按条件 whr=error 过滤出报错；φ:non_empty 只让非空结果流向下游，隐含"有才通知"。注：v0.1 语法卡没有显式条件分支语法，此写法是用过滤链近似表达"有就"，条件语义本身 [FAIL:uncertain]。）

### 4. 后台跑一个脚本，每30秒查一次状态，失败就重试最多3次

```
[RUN:@LOCAL|path=./job.sh]=>[WAIT|len=30s]=>[STAT:@PREV]=>[FAIL:task_failed|retry=yes]=>[RETRY|len=3]
```

（RUN=后台跑脚本；WAIT len=30s 等待轮询间隔；STAT 查上一步状态；失败按规范必须显式 [FAIL:...]，RETRY len=3 最多重试3次。注：v0.1 链式是线性单遍，"每30秒循环查询"的迭代语义无法严格表达，此处用 WAIT+STAT 单轮近似，循环语义 [FAIL:uncertain]。）

### 5. 读今天的日记文件，压缩成3条要点写到桌面

```
[READ:@SRC|path=./memory/diary/2026-09-25.md]=>[SUMM|len=3]=>[WRIT:@DST|path=~/Desktop/today_summary.md]
```

（READ 读今日日记 → SUMM len=3 压成3条 → WRIT 写到桌面路径，@DST 为输出去处。）
