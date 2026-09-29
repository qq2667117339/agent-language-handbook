# 轮0 · 互认测试评分（三家族全部完成）

> 测试设计：3 模型家族 × (5动词释义 + 5指令改写)，只凭 grammar_card.md + lexicon.md，零先验。
> 通过线：动词释义语义一致；指令改写结构一致率 >80%（动词选择+链式顺序一致，参数细节允许差异）。
> 注：qwen 名额原计划本地 qwen3.8:27b，因 Ollama 未运行+网关重启连续 4 次失败，改用云端 qwen3.7-flash（底层仍为阿里 Qwen 家族）。

## 动词释义（3/3 家族）

| 动词 | deepseek-v4-flash | glm-5.3-flash | qwen3.7-flash | 一致 |
|:--|:--|:--|:--|:--|
| READ | 读取文件内容(path/fmt/whr) | 读取文件内容(path/fmt/whr) | 读取文件内容(路径/格式/过滤) | ✅ |
| MERG | 合并多源(src/dst) | 多源合为一个(src/dst) | 多源合并为一个输出 | ✅ |
| FAIL | 报错必须给原因，不许沉默 | 报错必须给原因，禁止沉默 | 报错需附原因 | ✅ |
| SPWN | 调度子智能体(dst=简报路径) | 派生子智能体(dst=简报路径) | 调度子智能体执行任务 | ✅ |
| SUMM | 摘要压缩(len=条数/字数) | 摘要压缩(len=条数/字数) | 摘要(条数/字数) | ✅ |

**动词互认：5/5（三家族零分歧）**

## 指令改写（三方两两对比）

| # | deepseek | glm | qwen | 三方判定 |
|:--|:--|:--|:--|:--|
| 1 | LIST=>READ=>Σ=>WRIT=>Ω | LIST=>READ=>MERG(dst)=>Ω | LIST=>Σ(dst,path)=>Ω | △ 开头/合并一致，写盘表达 3 种分歧 |
| 2 | [θ]=>SUMM=>Ω | [XLAT]=>SUMM=>Ω | [θ]=>SUMM（漏Ω） | ✅ 主体一致（θ=XLAT 等价；qwen 漏终点） |
| 3 | FIND=>φ=>NOTE=>Ω ⚠ | READ=>φ=>NOTE ⚠ | FIND=>φ=>NOTE ⚠ | ✅ 链式全一致；检索动词 2:1 分歧；三家全标 uncertain |
| 4 | RUN=>ψ=>μ=>ζ=>Ω ⚠ | RUN=>WAIT=>STAT=>FAIL=>RETRY ⚠ | ξ+WAIT+ζ ⚠ | △ 三家全标 uncertain（循环盲区共识），动词大同小异 |
| 5 | READ=>SUMM=>WRIT=>Ω ⚠ | READ=>SUMM=>WRIT | READ(@MEM)=>SUMM=>WRIT | ✅ 结构全一致 |

**结构一致率（两两配对平均）：deepseek↔glm 90% / deepseek↔qwen 80% / glm↔qwen 80% → 平均 ≈83%**

**验收：>80% 通过 ✅（过线但有明确改进点，见下）**

## 关键发现（喂给轮2复盘）

1. **三家独立标注了同样的 [FAIL:uncertain] 盲区（三家族共识，高置信）**：
   - 条件分支（"有就通知"）— 语法卡无 IF 语法
   - 循环（"每30秒查一次"）— 链式是线性单遍，无 LOOP 语法
   → 轮2 复盘高优先提案：补 `[IF:cond]` 与 `[LOOP|every=30s,max=N]`
2. **写盘表达分歧**（WRIT 独立步 vs MERG dst 直接落盘）：MERG 能否直接落盘未定义 → 补语义表
3. **检索动词分歧**（FIND vs READ，2:1）：FIND 示例少 → 语法卡补示例
4. **qwen 漏 Ω 终点**：语法卡需强调"链必须以 Ω 结尾"（当前只在示例里隐含）
5. **参数笔误**（deepseek token=3 vs len=3）：语法卡补一行参数速查表
