# MiaoLang 语用规则 v1.1 (pragmatics)

## 0. 编码与路径（v1.1 新增）
- **UTF-8 强制**：所有消息与落盘文件强制 UTF-8（无 BOM）；中文入 ::UNTRUSTED{} 前后必须保持 UTF-8，出现乱码 = [FAIL:encoding]
- **路径别名 @ALIAS**：握手时可用 ::ALIAS{短名:实际路径} 声明短别名（如 ::ALIAS{@LAB:.}），后续消息用短名引用，消 token 黑洞；别名表随 ::STATUS 同步更新

## 1. 握手流程
```
[PING:lang=MiaoLang,ver=X.Y,cap=Ln]
  ├─ 对方同语言且 ver ≥ 本地 → [PONG:cap=Lm]
  ├─ 对方不认识本语言 → 教学流程：发 grammar_card.md 路径 + 最小对话示例，等对方 [PONG]
  └─ 30s 无应答 → [FAIL:no_pong|fallback=natural_language]
```

## 2. 能力分级
- **L0 旁听**：只读日志/旁听对话，可发 ? 元语言查询，不发操作
- **L1 基本操作**：READ/WRIT/LIST/CNT 等数据操作 + ACK/FAIL
- **L2 声明+复盘**：L1 + ::STATUS/::BUDGET/::PROPOSAL + 参与复盘讨论
- **L3 验证+投票**：L2 + [VALD] + ⊕/⊖ 投票 + 规范写入
- 分级由 PING 时自报，虚报能力 ⇒ 发现后降为 L0

## 3. 降级矩阵
| 场景 | 出路一 | 出路二 |
|:--|:--|:--|
| 解析失败 | [FAIL:parse_fail] → 发方用自然语言重说 | 双方切自然语言完成本轮，复盘时补语法 |
| 预算耗尽 | 砍修饰符只留动词链 | 拆成多条短消息 |
| 能力不足 | 降级发给能级更高的成员 | ::STATUS{state:blocked} 挂起等复盘 |

## 4. 预算声明
```
::BUDGET{tokens:N|pressure:low|mid|high}
```
- 每轮任务简报必须带 ::BUDGET
- pressure 阶梯：low=自然语言60%预算 / mid=40% / high=25%
- 发方超预算 ⇒ 消息作废，必须重写更短版本

## 5. 复盘会（postmortem）规程
- 时机：每轮任务结束后，进入预算外的安静时间
- 议程：① 统计本轮 token 消耗与失败点 ② 各成员提 ::PROPOSAL ③ 试用验证 [VALD] ④ 投票 ⑤ 版本 +0.1 写 changelog
- 元语言讨论自由：允许用自然语言讨论语言本身（手册允许，语言规范管任务通信，不管复盘）

## 6. 传播/教学协议
- 新成员接入首选：旁听 2-3 轮真实对话日志（runs/ 目录）
- 规范文档是兜底教材，不是首选
- 新成员允许随时发 `?X` 查询符号含义，老成员有问必答（教学义务）

## 7. 人类可读注释约定
- 所有落盘 .ml 消息文件，允许在下方追加 `# 注释: ...` 行（不参与解析，仅供人看）
