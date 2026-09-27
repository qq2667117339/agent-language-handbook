# 轮2 · 复盘会材料 — 提案池与投票规程

> 依据：轮0互认测试（三家族共识盲区）+ 轮1实测（run1_report.md）。
> 你的身份：语言委员会成员（cap=L3）。你的产出：新提案 + 对池内提案的投票。

## 已知问题（实证来源）

| # | 问题 | 来源 |
|:--|:--|:--|
| P1 | 条件分支无语法（"有就通知"无法表达） | 三家族互认测试共识盲区 |
| P2 | 循环无语法（"每30秒查一次"只能线性近似） | 三家族互认测试共识盲区 |
| P3 | MERG 能否直接 dst 落盘未定义（三家写法分歧） | 互认测试指令1 |
| P4 | FIND vs READ 分工模糊（2:1 使用分歧） | 互认测试指令3 |
| P5 | 链是否必须 Ω 结尾未强制（qwen 漏终点） | 互认测试指令2 |
| P6 | 参数槽位易笔误（len 被写成 token） | 互认测试 deepseek |
| P7 | ::UNTRUSTED{} 中文 mojibake（编码无规范） | 轮1实测 worker-A 回执 |

## 立法者（妙）预置提案

::PROPOSAL{sym:[IF:cond]=>[A]|meaning:cond成立才执行A,否则跳到下一独立段|reason:补P1盲区,三家共识}
::PROPOSAL{sym:[LOOP|every=30s,max=N]=>[A]=>[μ]|meaning:每30s执行A并查状态,最多N轮,失败走[FAIL]|reason:补P2盲区,三家共识}
::PROPOSAL{sym:[Σ|dst=路径]|meaning:MERG 支持 dst 直接落盘,等价 MERG=>WRIT 两步合并|reason:补P3,减少一笔}
::PROPOSAL{sym:[FIND:@X|whr=k]|meaning:FIND=在@X内容里检索关键词;READ=整读文件。分工写死进语义表|reason:补P4}
::PROPOSAL{sym:Ω强制|meaning:任务链必须以[Ω]结尾,缺Ω=链未完成,接收方必须[FAIL:no_terminal]|reason:补P5}
::PROPOSAL{sym:参数速查|meaning:语法卡末尾附一行:仅 path/mch/fmt/len/whr/src/dst/lng/retry/fallback/out 11个槽位|reason:补P6}

## 投票规程

1. 对上述每条预置提案：⊕（同意）或 ⊖（反对）+ 一句理由（≤30字）
2. 你可另提 0-2 条新提案（格式 ::PROPOSAL{sym:X|meaning:Y|reason:Z}），解决你没看到被覆盖的问题
3. 判定标准：省 token 且不引入歧义 → ⊕；只省 token 但歧义风险高 → ⊖；只加清晰度不省 token → 可以 ⊕（清晰度也是资产）
4. 门槛：≥2/3 委员同意 → 写入规范 v1.1
