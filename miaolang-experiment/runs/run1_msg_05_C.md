::BUDGET{tokens:150|pressure:mid}
::STATUS{@TASK|state:running|round:1}
[READ:@SRC|path=.\runs\run1_output.md]=>[READ:@SRC|path=.\runs\run1_merged.md]=>[VALD:@PREV|method=source_check]=>[Ω]
# 注释: 读3条要点(run1_output.md) → 对照合并原文(run1_merged.md, 68KB, 分段读第3/4/7章重点) → 验证要点是否忠于原文
# 验证标准: 每条要点判 忠实/偏差/编造, 附一句依据(引用原文关键词)
# 回执要求: [VALD] + 3条判定 + ⊕(整体通过)或⊖(打回), 写入 runs\run1_msg_06_miao.md
