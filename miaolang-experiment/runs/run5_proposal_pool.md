# 轮5 · 复盘会材料 — 提案池与投票规程

> 实证来源：轮4报告（run4_report.md）。核心确认问题：双 READ 串联 @PREV 覆盖前源（B链+C验证双重确认）。
> 你的身份：语言委员会成员（cap=L3）。产出：对预置提案投票 + 可提新提案。

## 立法者（妙）预置提案

::PROPOSAL{sym:@PREV2|meaning:历史槽位,@PREV=最近一源,@PREV2=前一源,@PREV3=再前一,链式多源读取不丢数据|reason:轮4 GAP1实证,双READ覆盖前源}
::PROPOSAL{sym:多源显式规则|meaning:链中≥2个READ/FIND时,后续步骤引用多源必须显式src=@PREV,@PREV2或Σ|src=列表,禁止隐式依赖|reason:与@PREV2互补,写进语法卡禁止区}
::PROPOSAL{sym:VALD扩权|meaning:VALD验证员判定可标注 驳回原因类型(偏差/编造/过度推断),写入回执供复盘统计|reason:轮3/轮4验证已自发这么做,规范化}
::PROPOSAL{sym:域标签|meaning:任务消息可带::DOMAIN{type:code-analysis|info-retrieval|...}声明任务域,帮助成员预判该域常用动词|reason:轮4观察到跨域适应性可显式化}

## 投票规程

1. 对 4 条预置提案逐条：⊕/⊖ + 一句理由（≤30字）
2. 可提 0-2 条新提案（::PROPOSAL{sym:X|meaning:Y|reason:Z}），必须附实证来源
3. 判定标准：省 token 且不引入歧义 → ⊕；只省 token 但歧义风险高 → ⊖；只加清晰度不省 token → 可以 ⊕
4. 门槛：≥2/3 通过 → 写入规范 v1.2
