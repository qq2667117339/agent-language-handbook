# mutual_test_deepseek

> 依据：仅 grammar_card.md + lexicon.md。未定义用法一律标 [FAIL:uncertain]。

## 动词释义（5条）

1. **READ** — 读取文件内容（参数 path/fmt/whr），即把指定路径的文件读进来作为数据源。
2. **MERG**（别名 Σ）— 合并多源，把多个输入源汇成一个（参数 src/dst）。
3. **FAIL** — 报告错误，失败时必须显式声明原因（参数 whr=原因），不许沉默。
4. **SPWN** — 调度子智能体，把任务简报（dst=简报路径）派给一个子智能体去跑。
5. **SUMM** — 摘要，把输入压缩成若干条/若干字（参数 len=条数或字数）。

## 指令改写（5条）

### 1. 读取 data 目录下所有 csv，合并成一个文件
```
[LIST:@SRC|path=./data,mch=*.csv]=>[READ]=>[Σ]=>[WRIT:@DST|path=./merged.csv,fmt=csv]=>[Ω]
```

### 2. 把上一条结果翻译成英文，摘要成3点
```
[θ|src=@PREV,lng=en]=>[SUMM|len=3]=>[Ω]
```

### 3. 检查日志里有没有报错，有就通知我
```
[FIND:@LOG|whr=error]=>[φ:non_empty]=>[NOTE:@USER|len=1]=>[Ω]
```
（"有就通知"的条件分支未在语法卡中定义，条件触发式 NOTE 属推断用法 → [FAIL:uncertain]）

### 4. 后台跑一个脚本，每30秒查一次状态，失败就重试最多3次
```
[RUN:@LOCAL|path=./script]=>[ψ|len=30s]=>[μ|src=@PREV]=>[ζ|len=3]=>[Ω]
```
（"每30秒"的循环语义未定义，ψ 只写"等待轮询"；RUN→WAIT→STAT 的循环未在语法卡给出 → [FAIL:uncertain]）

### 5. 读今天的日记文件，压缩成3条要点写到桌面
```
[READ:@LOCAL|path=./diary/today.md]=>[SUMM|len=3]=>[WRIT:@DST|path=./Desktop,token=3]=>[Ω]
```
（"写到桌面"的目标路径未在实体表中定义，@DST 可指输出去处但桌面路径无标准槽位 → [FAIL:uncertain]）
