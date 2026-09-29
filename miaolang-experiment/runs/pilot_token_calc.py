# -*- coding: utf-8 -*-
"""A/B pilot token comparison"""
try:
    import tiktoken
    enc = tiktoken.get_encoding("cl100k_base")
    count = lambda s: len(enc.encode(s))
except ImportError:
    count = lambda s: len(s) // 2  # rough CJK estimate

nl_brief = """读取 <MEMORY>\\2026-09-25.md 的完整内容，统计整个文件的字符总数（含中文和符号，不含空白符），然后提炼出 2026-09-25 当天最重要的 3 条核心事件（每条不超过 50 个字，要具体，不要空话），最后把统计结果和 3 条摘要写入 <MEMORY>\\notes\\2026-09-25-summary-nl.md（如果 notes 目录不存在就创建），文件格式：第一行写"字符统计: N"，空一行后写 3 条摘要（每条一行，前面加序号）。写完后用 read 工具回读该文件确认内容存在，确认成功才算完成。完成后回复我：统计数字 + 3 条摘要的原文。"""

ml_msg = """[READ:@MEM\\2026-09-25.md]=>[CNT|whr=chars_no_space]=>[SUMM|len=3]=>[WRIT:@MEM\\notes\\2026-09-25-summary.md]=>[Ω]
# 注释: 读9-25记忆 → 统计字符数(不含空白符) → 摘要3条当天核心事件(每条≤50字,要具体) → 结果写入notes目录(不存在则创建,格式:第一行"字符统计: N",空行,3条带序号摘要)
# 回执: [ACK]+统计数字+3条摘要 → 直接回复给我"""

mini_card = open(r".\spec\grammar_card_mini.md", encoding="utf-8").read()

rows = [
    ("NL brief (instruction only)", count(nl_brief)),
    ("ML message (instruction only)", count(ml_msg)),
    ("ML mini-card injection (one-time)", count(mini_card)),
    ("ML total for 1 task", count(ml_msg) + count(mini_card)),
    ("ML total for 3 tasks (card amortized)", count(ml_msg) * 3 + count(mini_card)),
    ("NL total for 3 tasks", count(nl_brief) * 3),
]
out = "\n".join(f"{n}: {t}" for n, t in rows)
print(out)
nl1, ml1 = count(nl_brief), count(ml_msg) + count(mini_card)
nl3, ml3 = count(nl_brief) * 3, count(ml_msg) * 3 + count(mini_card)
print(f"\n1-task: NL {nl1} vs ML {ml1} -> ML {'saves' if ml1<nl1 else 'costs'} {abs(nl1-ml1)}")
print(f"3-task: NL {nl3} vs ML {ml3} -> ML {'saves' if ml3<nl3 else 'costs'} {abs(nl3-ml3)} ({nl3/ml3:.2f}x)")
