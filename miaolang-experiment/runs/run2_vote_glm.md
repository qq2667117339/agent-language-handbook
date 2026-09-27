# 委员2 glm 投票

> 依据：grammar_card v0.1 / lexicon v0.1 / semantics v0.1 + run1 实测报告。独立判定，标准：省token且无歧义→⊕；省token但歧义高→⊖；纯增清晰度→可⊕。

## 对预置提案

P1: ⊕ 补真实盲区；但须写明IF假⇒该链免Ω，防与Ω强制冲突
P2: ⊕ max=N防死循环，终止可判定，补真实盲区
P3: ⊕ 省一步；建议改用out=槽，免dst承载双重语义
P4: ⊕ 纯消歧零成本，写死进语义表
P5: ⊕ 漏终点轮1实测发生过，机械可判，5token值得
P6: ⊕ 规范内一行零消息成本；cond/every/max新槽须同步入表

## 新提案

::PROPOSAL{sym:UTF8强制|meaning:所有MiaoLang消息含::UNTRUSTED{}内容一律UTF-8编码，禁GBK/混编码，检测到乱码接收方回[FAIL:encoding]|reason:补P7盲区，轮1实测中文文件名mojibake，池内6条均未覆盖}

::PROPOSAL{sym:路径别名|meaning:PING握手可附alias声明(如W=C:\Users\...\workspace)，全链消息用@W指代长路径，用户别名限1-2字符且不得与实体表冲突|reason:轮1压缩比仅1.3x，Windows绝对路径是最大token黑洞，high档前先备好机制}
