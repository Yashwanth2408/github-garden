# github-garden

A living repository that grows a little every day.

This is my digital dev garden — a place where algorithms get planted, utility functions bloom, and learning notes accumulate. It grows automatically through a GitHub Actions workflow that waters it multiple times a day, keeping the contribution graph consistently green.

## What's Growing Here

| Plot | Description |
|------|-------------|
| `algorithms/` | Classic algorithms in Python — sorting, graphs, trees, DP, strings |
| `snippets/` | Reusable utility functions for everyday programming |
| `logs/` | Daily TIL entries and dev notes |
| `stats/` | Contribution metrics and streak tracking |

## How It Works

A GitHub Actions workflow triggers 5 times per day. Each run independently decides whether to commit using a day-of-week weighted oracle — not every trigger commits, which is what makes the pattern look like a real developer.

When a commit does happen, it adds actual content:

- A new algorithm implementation with docstring and complexity notes
- A utility function added to the snippets library
- A TIL (Today I Learned) entry in the dev log
- Updated contribution stats and streak counter

The commit timestamps are jittered ±25 minutes around each trigger window so the activity heatmap looks natural, not mechanical.

**Expected pattern:** 2–3 commits on busy weekdays, 1–2 on Fridays, lighter on weekends, with occasional full rest days — about 1–2 per month.

## Stats

See [stats/README.md](stats/README.md) for live metrics.

## Plots at a Glance

```
algorithms/
  sorting.py      — bubble, insertion, merge, quick, heap, radix, shell
  graphs.py       — BFS, DFS, Dijkstra, topological sort, union-find
  trees.py        — BST, trie, LCA, level-order, serialize/deserialize
  dp.py           — Fibonacci, LCS, knapsack, edit distance, Kadane, LIS
  strings.py      — KMP, Z-algorithm, anagram detection, palindromes

snippets/
  string_utils.py   — slugify, truncate, camel_to_snake, chunk_list, memoize
  file_utils.py     — safe_read, hash_file, atomic_write, retry, deep_merge
  datetime_utils.py — humanize_delta, date_range, next_business_day
  cli_utils.py      — progress_bar, color_print, table_print, spinner

logs/
  YYYY-MM.md      — monthly dev logs with TIL entries
```

---

*Planted with care. Watered by automation.*
