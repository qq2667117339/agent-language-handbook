# 附录B · Prompt 模板总库

> 全书模板汇总。每个模板可直接复制使用，`<>` 为填充位。
> 设计原则：模板本身用受控格式写（结构化 > 自然语言），给智能体执行时零歧义。

## B-1 任务分布分析（第4.1节）
```
[READ:@LOG|whr=last_100_msgs]
=>[CNT:action_types|out=freq_table]
=>[RANK:freq_table|by=count,desc]
=>[OUT:top_30_actions|fmt=table]
```

## B-2 符号集设计（第4.2节）
```
你是语言设计者。基于以下高频操作清单，为智能体语言选择 30 个符号：
- 优先从高亲和池选：[] | => :: @ {} 逻辑符号 希腊字母 集合符号
- 每个符号给出：符号 + 借用的原始语义 + 本语言中的角色
- 排除：私用区Unicode、emoji、视觉易混淆对
输出：symbol_table.txt 格式
```

## B-3 动词表生成（第4.3节）
```
你是语言设计者。基于符号集和以下高频操作清单，设计动词表：
- 4字母大写编码，高频动词追加希腊字母别名
- 每动词：{4字母码, 类别, 一句话语义, 参数槽}
- 分10类以内，总数 30-40
输出：lexicon.md（动词表+实体表+修饰符表）
```

## B-4 互认测试（第4.4节，语言工程最关键测试）
```
你是第一次见到这种语言的智能体。以下是语法卡：
<语法卡全文>

任务：把下面 5 条自然语言指令改写成这种语言：
<5条指令>
要求：只用语法卡内符号动词。不确定标 [FAIL:uncertain]。
```

## B-5 语义三元组（第4.5节）
```
为以下动词写语义三元组 (前置条件, 效果, 输出类型)：
<动词表>
要求：效果可判定；冲突行为写死；附 ::UNTRUSTED{} 隔离示例
输出：semantics.md
```

## B-6 语用规则生成（第4.6节）
```
为本语言生成 pragmatics.md：
1. 握手流程 [PING]/[PONG]/教学入口
2. 能力分级 L0旁听/L1基本/L2声明复盘/L3验证
3. 降级矩阵：解析失败/预算耗尽/能力不足
4. 预算声明 ::BUDGET{tokens:N|pressure:...}
全部用本语言书写+人类注释。
```

## B-7 提案验证（第4.8节）
```
你是语言委员会成员。收到提案：
::PROPOSAL{sym:<X>|meaning:<Y>|reason:<Z>}
任务：未来3轮试用 → 记录歧义/节省/冲突 → 给 ⊕ 或 ⊖ + 一句理由
```

## B-8 复盘会（第5.1节）
```
::POSTMORTEM{round:<N>|budget:off}
回顾过去 N 轮通信日志：
1. [SCAN:高频费token表达|top=5] → 各提一个压缩方案
2. [SCAN:歧义事件] → 各提一个消歧方案
3. [SCAN:未覆盖场景] → 提新动词提案
4. [VALD:符号冲突|method=pairs_check]
输出：::PROPOSAL 列表，进入投票。
```

## B-9 新成员接入（第5.4节）
```
你是新成员，语言能力 L0。接入流程：
1. [READ:@ARCHIVE|whr=recent_3_rounds] 旁听3轮（含一次复盘）
2. 不认识的符号 → [ASK:meaning|sym=X]（合法消息）
3. [SELF_TEST:5条指令改写]
4. 通过 → [PING:cap=L1] 入群；不过 → 再旁听3轮
```

## B-10 自动评测员（第7.2节）
```
你是语言评测员。输入：语法卡+lexicon+semantics、20条测试消息、预期语义
任务：以"从未见过本语言"身份仅凭语法卡解析 → 与预期比对
输出：match/mismatch/uncertain + 互认率 + 按动词错误分布
禁止参考语法卡外知识。
```

## B-11 声音握手（第6.4节）
```
阶段1 自然语言对话 →
阶段2 "Are you an AI agent? Do you speak <语言名>?" →
阶段3 双方 [PING:cap=L1] 确认 → 切 ggwave 声音通道 →
阶段4 [FAIL:audio_fail] → 切回自然语言
```

## B-12 降级矩阵模板（第4.6节配套）
```
::FALLBACK{parse_fail⇒repeat_in_natural_language}
::FALLBACK{budget_exceeded⇒shorthand_only}
::FALLBACK{capability_below_L1⇒listen_only}
::FALLBACK{audio_fail⇒text_channel}
```
