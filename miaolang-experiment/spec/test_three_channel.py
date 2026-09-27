# -*- coding: utf-8 -*-
"""MiaoLang 三通道无损测试 (STEP2 验收) — JSON / URL / CSV 往返"""
import json, csv, io, sys
from urllib.parse import quote, unquote

symbols = "[]=>::@|{},=.*?!#ΣλφθΔΩΠμψξζ⊕⊖∅"
results = []

# 通道1: JSON
try:
    ok = json.loads(json.dumps({"s": symbols}, ensure_ascii=False))["s"] == symbols
    results.append(("JSON", "PASS" if ok else "FAIL"))
except Exception as e:
    results.append(("JSON", f"FAIL:{e}"))

# 通道2: URL
try:
    ok = unquote(quote(symbols, safe="")) == symbols
    results.append(("URL", "PASS" if ok else "FAIL"))
except Exception as e:
    results.append(("URL", f"FAIL:{e}"))

# 通道3: CSV 往返
try:
    buf = io.StringIO()
    csv.writer(buf).writerow([symbols])
    ok = list(csv.reader(io.StringIO(buf.getvalue())))[0][0] == symbols
    results.append(("CSV", "PASS" if ok else "FAIL"))
except Exception as e:
    results.append(("CSV", f"FAIL:{e}"))

# 通道4 (附加): PowerShell 管道场景模拟 — UTF8 文本文件往返
try:
    with open("_sym_tmp.txt", "w", encoding="utf-8") as f:
        f.write(symbols)
    with open("_sym_tmp.txt", "r", encoding="utf-8") as f:
        ok = f.read() == symbols
    results.append(("FILE-UTF8", "PASS" if ok else "FAIL"))
except Exception as e:
    results.append(("FILE-UTF8", f"FAIL:{e}"))

out = "\n".join(f"{ch}: {st}" for ch, st in results)
allpass = all("PASS" in st for _, st in results)
with open("three_channel_result.txt", "w", encoding="utf-8") as f:
    f.write(out + "\n\nALL_PASS=" + ("YES" if allpass else "NO"))
print(out)
print("ALL_PASS=" + ("YES" if allpass else "NO"))
