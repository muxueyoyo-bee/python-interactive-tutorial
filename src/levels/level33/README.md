# 第三十三关: collections 数据结构

collections 模块提供比内置容器更强大的数据结构.

## Counter -- 计数器

```python
from collections import Counter
words = ["a", "b", "c", "a", "b", "a"]
count = Counter(words)
print(count.most_common(2))  # [('a', 3), ('b', 2)]
```

## 其他工具

| 类 | 用途 |
|------|------|
| Counter | 计数统计 |
| defaultdict | 带默认值的字典 |
| deque | 双端队列 |
| namedtuple | 具名元组 |

## 你的任务

用 Counter 统计列表词频, 输出出现最多的前 2 个元素.

预期输出:
```
[('a', 3), ('b', 2)]
```
