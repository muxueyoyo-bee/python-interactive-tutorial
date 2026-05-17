# 第三十八关: pandas Series

Pandas Series 是一个带标签的一维数组.

## 创建 Series

```python
import pandas as pd
s = pd.Series([10, 20, 30, 40, 50],
              index=["a", "b", "c", "d", "e"])
print(s)
```

## 基本操作

```python
print(s["a"])          # 按标签索引 -> 10
print(s.describe())    # 统计摘要 (count/mean/std/min/max)
```

## 你的任务

创建 Series 值[10,20,30,40,50]索引[a,b,c,d,e], 打印内容和统计摘要.

预期输出: Series 表格 + describe() 统计信息
