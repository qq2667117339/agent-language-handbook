# MiaoLang mapping（明文映射层 · 脚手架）

> 用途：debug 定位 + 版本迁移参照。不参与解析。
> 更新频率：每版本（群落可投票修改）。

## v0.1

```
[READ:@SRC|path=X] = 读取X的内容
[LIST:@LOCAL|mch=*.md] = 列出本地全部md文件
[φ:non_empty] = 过滤掉空段落
[Σ] = 合并全部内容
[SUMM|len=3] = 生成3条要点摘要
[Ω] = 输出结果
=> = 把上一步的输出交给下一步
::BUDGET{tokens:N|pressure:P} = 本轮预算N tokens，压力档P
[PING/PONG] = 语言握手/应答
[ACK] = 确认收到/完成
[FAIL:reason] = 报告失败及原因
[RETRY|len=3] = 最多重试3次
[NOTE:@USER|len=短] = 通知用户一句话
```

## 手册对照（00页预期形态）

自然语言原句：
> 读取本地全部md文档，过滤掉空段落，合并内容，生成3条要点摘要输出

MiaoLang v0.1 改写：
`[LIST:@LOCAL|mch=*.md]=>[φ:non_empty]=>[Σ]=>[SUMM|len=3]=>[Ω]`
