# 第四十二关: pandas merge 合并

merge() 类似 SQL 的 JOIN -- 根据共同的列将两张表合并.

## 合并两张表

```python
import pandas as pd
left = pd.DataFrame({"id": [1,2,3], "name": ["Alice","Bob","Charlie"]})
right = pd.DataFrame({"id": [1,2,3], "score": [85,92,78]})
merged = pd.merge(left, right, on="id")
print(merged)
```

## 合并类型

| how= | 含义 |
|------|------|
| inner | 交集(默认) |
| left | 保留左表所有行 |
| right | 保留右表所有行 |
| outer | 并集 |

## 你的任务

将两张表按 id 合并, 打印合并结果.

预期输出: 合并后的完整 DataFrame
