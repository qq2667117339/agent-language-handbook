# run6 失败模式分析（worker-A）

## 检索范围
runs/ 目录全部 *.md，检索关键词 FAIL

## 失败模式类型统计
- parse_fail: 1 次（run1_report，解析失败率 0% 记录）
- file_not_found: 0 次
- timeout: 0 次
- other: 13 次
  - uncertain: 3
  - old_version: 1
  - audio_fail: 2
  - no_terminal: 2
  - encoding: 2
  - no_evidence: 2
  - max_reached: 1

## 观察（各≤40字）
1. other(13) 绝对主导，file_not_found/timeout 零实例，缺执行层失败样本。
2. parse_fail 仅1次(轮1)，群落解析成熟，其余多为规范设计讨论。