::BUDGET{tokens:150|pressure:mid}
::STATUS{@TASK|state:running|round:1}
[LIST:@SRC|path=<DESKTOP>\智能体语言资料\06_论文成品,mch=*.md]=>[READ]=>[φ:non_empty]=>[Σ|dst=@PREV]=>[WRIT:@DST|path=.\runs\run1_merged.md]=>[Ω]
# 注释: 列出论文成品目录全部md → 读取 → 过滤空段 → 合并 → 写入 run1_merged.md
# 回执要求: [ACK] + files=数量，写入 runs\run1_msg_02_miao.md
