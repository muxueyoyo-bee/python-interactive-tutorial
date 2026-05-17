# 第三十关: itertools 实用工具

itertools 是一组高效迭代器工具, 用于排列, 组合等场景.

## combinations -- 组合

```python
from itertools import combinations, permutations
items = ["A", "B", "C"]
print(list(combinations(items, 2)))
# [('A','B'), ('A','C'), ('B','C')] -- 不考虑顺序
```

## permutations -- 排列

```python
print(list(permutations(items, 2))[0])
# ('A', 'B') -- 考虑顺序
```

组合 vs 排列: AB和BA在组合中算同一种, 排列中算两种.

## 你的任务

对 ["A","B","C"] 取出所有 2 组合和第一个 2 排列, 分别打印.

预期输出:
```
[('A', 'B'), ('A', 'C'), ('B', 'C')]
('A', 'B')
```
