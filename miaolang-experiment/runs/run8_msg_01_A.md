::BUDGET{tokens:45|pressure:high}
[FIND:@LAB\runs|whr=ZZZNOHIT9]
[LIST:@LAB\runs|mch=run1_msg_*.md]=>[READ]=>[φ:non_comment]=>[Σ|out=@LAB\runs\run8_merged.md]=>[Ω]
# 注释: 第一行=∅实测(无命中,期望返回∅而非FAIL)；主链=轮3同款标准链(v1.3语法重跑对照)
# 回执: [ACK]+∅结果+files/bytes → run8_msg_02_miao.md，预算45内
