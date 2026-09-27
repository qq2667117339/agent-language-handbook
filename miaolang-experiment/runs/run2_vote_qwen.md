# 委员3 qwen 投票
## 对预置提案
P1: ⊕ 补条件分支盲区，语义清晰，三家共识
P2: ⊖ [μ]轮询位置歧义大：每轮都查还是仅末次？语义未定死
P3: ⊕ 一步省一笔，MERG直写dst语义无二义
P4: ⊕ FIND/READ分工写死，高频动词防混用
P5: ⊕ Ω强制终了简单有效，缺链必报FAIL
P6: ⊕ 不省token但补槽位速查，笔误率可降

## 新提案
::PROPOSAL{sym:UTF-8强制|meaning:所有MiaoLang消息编码强制UTF-8，解析器遇非UTF-8字节序列⇒[FAIL:encoding]|reason:补P7编码漏洞，彻底消灭mojibake}
::PROPOSAL{sym:@NEXT定义|meaning:@NEXT在链中显式指向当前步骤输出供后续引用；缺省链中自动传递@PREV仍保留|reason:链式数据流@PREV隐式传递，显式命名更安全}
