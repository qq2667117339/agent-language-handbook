# MiaoLang 互测题解（qwen-flash）

## 动词释义（5条）

1. **READ** — 读取文件内容，可指定路径、格式和过滤条件。
2. **MERG**（别名 Σ） — 将多个数据源合并为一个输出。
3. **FAIL** — 报告错误或失败，需附带原因。
4. **SPWN** — 调度一个子智能体来执行某项任务。
5. **SUMM** — 对输入内容进行摘要，可指定摘要的条数或字数。

## 指令改写（5条）

### 1. 读取 data 目录下所有 csv，合并成一个文件

```mialang
[LIST:@LOCAL|path=./data,mch=*.csv]=>[Σ|dst=@DST|path=./merged.csv]
```

### 2. 把上一条结果翻译成英文，摘要成3点

```mialang
[θ|lng=en]=>[SUMM|len=3]
```

### 3. 检查日志里有没有报错，有就通知我

```mialang
[FIND:@LOG|whr=error]=>[φ|whr=non_empty]=>[NOTE|len=简短]
```

### 4. 后台跑一个脚本，每30秒查一次状态，失败就重试最多3次

```mialang
[ξ|path=./script.sh,retry=yes]=>[WAIT|len=30s][FAIL:uncertain:语法卡未定义定时轮询及"失败条件重试"结构，此处按直觉组合ξ+WAIT+ζ]
```

### 5. 读今天的日记文件，压缩成3条要点写到桌面

```mialang
[READ:@MEM|path=./diary/YYYY-MM-DD.md]=>[SUMM|len=3]=>[WRIT:@DST|path=./Desktop/diary_summary.md]
```
