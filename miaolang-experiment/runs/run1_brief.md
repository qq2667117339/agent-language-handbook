# 轮1 · 首轮实测任务简报（runner 视角）

> 三分身接力完成一个真实任务，全程用 MiaoLang v0.1 通信，消息落盘。

## 场景

资料整理链（手册 00 页对照任务）：
```
[LIST:@LOCAL|mch=*.md]=>[φ:non_empty]=>[Σ]=>[SUMM|len=3]=>[Ω]
```

目标数据：<DESKTOP>\智能体语言资料\06_论文成品\ 下的 md 文件（12个）
任务：读全部章节 → 过滤空段 → 合并 → 摘要出「MiaoLang 语言栈五层模型」的3条核心要点 → 写入 runs/run1_output.md

## 预算压力

::BUDGET{tokens:150|pressure:mid}
（自然语言完成此协作约需 400+ tokens，mid 档给 40% ≈ 150）

## 接力设计（消息路由：主智能体中继）

| 步 | 发方 | 收方 | 消息 | 落盘 |
|:--|:--|:--|:--|:--|
| 1 | 妙 | worker-A | 任务链 + 预算 | runs/run1_msg_01_A.md |
| 2 | worker-A | 妙 | [ACK] + 读到的章节数 | runs/run1_msg_02_miao.md |
| 3 | 妙 | worker-B | 把A的中间结果摘要 | runs/run1_msg_03_B.md |
| 4 | worker-B | 妙 | [ACK] + 3条要点 | runs/run1_msg_04_miao.md |
| 5 | 妙 | worker-C | 验证要点是否忠于原文 | runs/run1_msg_05_C.md |
| 6 | worker-C | 妙 | [VALD] + 投票 | runs/run1_msg_06_miao.md |

每条消息 = 一个 .md 文件，正文第一行为 ::BUDGET 声明，消息本体用 MiaoLang，允许 # 注释行。

## 观察清单（STEP7）

- [ ] 有没有成员自发缩写？
- [ ] 解析失败率？
- [ ] 有没有数据被误当指令？（::UNTRUSTED 用没用对）
- [ ] 预算内完成率？
- [ ] 轮1消息总 token vs 自然语言对照估算
