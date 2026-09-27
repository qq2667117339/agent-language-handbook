::BUDGET{tokens:60|pressure:high}
[LIST:@LAB\runs|mch=run1_msg_*.md]=>[READ]=>[φ:non_comment]=>[Σ|out=@LAB\runs\run3_merged.md]=>[Ω]
# 注释: 列轮1全部消息文件 → 读 → 滤掉#注释行 → 合并落盘(用v1.1的out=直落)
# 回执: [ACK]+files/bytes → run3_msg_02_miao.md，预算60内
