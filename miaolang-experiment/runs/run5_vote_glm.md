# 委员2 glm 投票

> 依据：grammar_card v1.1 / lexicon v1.1 / semantics v0.1 / run4_report。独立判断，未迎合立法者。

## 对预置提案

P1: ⊕ 真实缺口双重实证；但须写死 @PREVn 按数据步骤计数，防中间过滤步搅乱序号
P2: ⊕ 防隐式依赖返工，与P1互补；应注明 @PREV2 即属"显式引用"，免两规打架
P3: ⊕ 已有实践规范化，结构化标注省token且回执可统计
P4: ⊖ 轮4实证跨域零解析失败，无问题支撑；净增token且收到后无强制行为

## 新提案

::PROPOSAL{sym:∅注册|meaning:∅注册为标准符号(入symbol_table+语法卡),语义=操作成功但结果为空,与FAIL(操作失败)显式区分|reason:semantics.md FIND条目已用∅,但语法卡禁止区第3条禁未注册符号,规范自相矛盾}

::PROPOSAL{sym:FAIL_max_reached不重试|meaning:写死[FAIL:max_reached]携带retry=no,LOOP的max即重试预算,FAIL不再叠加指数退避|reason:semantics.md中FAIL(退避3次)与LOOP(达max即停)交互未定义,双重重试会白烧token}

---
*委员2 glm (cap=L3) · 2026-09-25*
