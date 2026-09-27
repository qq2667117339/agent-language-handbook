# -*- coding: utf-8 -*-
"""v1.4 新别名三通道测试: chi sigma eta"""
import json, csv, io
from urllib.parse import quote, unquote
symbols = "χση"
results = []
ok1 = json.loads(json.dumps({"s": symbols}, ensure_ascii=False))["s"] == symbols
results.append(("JSON", "PASS" if ok1 else "FAIL"))
ok2 = unquote(quote(symbols, safe="")) == symbols
results.append(("URL", "PASS" if ok2 else "FAIL"))
buf = io.StringIO(); csv.writer(buf).writerow([symbols])
ok3 = list(csv.reader(io.StringIO(buf.getvalue())))[0][0] == symbols
results.append(("CSV", "PASS" if ok3 else "FAIL"))
out = "\n".join(f"{c}: {s}" for c, s in results)
allpass = all("PASS" in s for _, s in results)
print(out); print("ALL_PASS=" + ("YES" if allpass else "NO"))
