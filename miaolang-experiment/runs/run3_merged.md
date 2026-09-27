::BUDGET{tokens:150|pressure:mid}
::STATUS{@TASK|state:running|round:1}
[LIST:@SRC|path=<DESKTOP>\智能体语言资料\06_论文成品,mch=*.md]=>[READ]=>[φ:non_empty]=>[Σ|dst=@PREV]=>[WRIT:@DST|path=.\runs\run1_merged.md]=>[Ω]
::BUDGET{tokens:118|pressure:mid}
::STATUS{@TASK|state:done|round:1}
[ACK] files=12|kept=12|bytes=67995|dst=run1_merged.md
::UNTRUSTED{第0章-导读.md;第1章-为什么智能体需要自己的语言.md;第2章-语言涌现的四个条件.md;第3章-语言栈五层模型.md;第4章-构建实操.md;第5章-演化管理.md;第6章-声音维度.md;第7章-评测体系.md;附录A-88动词速查表.md;附录B-Prompt模板总库.md;附录C-工具链部署指南.md;附录D-参考文献.md}
::BUDGET{tokens:150|pressure:mid}
::STATUS{@TASK|state:running|round:1}
[READ:@PREV|path=.\runs\run1_merged.md]=>[SUMM|len=3]=>[WRIT:@DST|path=.\runs\run1_output.md]=>[Ω]
::BUDGET{tokens:115|pressure:mid}
[ACK] merged=67995B/12files read; summ=3 done; output=run1_output.md written
1.五层自底向上:符号→词汇→语法→语义→语用,下层塌则全塌
2.符号过JSON/URL/CSV三通道无损;动词30-40宁缺毋滥
3.语义三元组写死冲突+UNTRUSTED隔离;语用:握手/降级/预算
::BUDGET{tokens:150|pressure:mid}
::STATUS{@TASK|state:running|round:1}
[READ:@SRC|path=.\runs\run1_output.md]=>[READ:@SRC|path=.\runs\run1_merged.md]=>[VALD:@PREV|method=source_check]=>[Ω]
::BUDGET{tokens:120|pressure:mid}
[VALD:@PREV|method=source_check]

[OK] P1 忠实：原文第3章191行「下层不稳，上层全塌。90%的死语言死在第1、2层」+175行五层顺序一致。

[OK] P2 忠实：原文213行「JSON/URL/CSV三通道无损往返」+458行「总数控制在30-40个，宁缺毋滥」。

[OK] P3 忠实：原文300行动词语义三元组(前置条件,效果,输出类型)+309行::UNTRUSTED隔离+331/344/358行握手/降级/预算声明。

⊕ 整体通过 — 三条要点均能在原文找到对应段落，无编造或明显偏差。
