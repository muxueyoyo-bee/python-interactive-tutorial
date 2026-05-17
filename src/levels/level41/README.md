# 第四十一关: pandas groupby 分组

groupby() 类似 SQL 的 GROUP BY -- 按某列分组, 然后对每组做聚合计算.

## 分组聚合

```python
import pandas as pd
df = pd.DataFrame({"部门": ["A","B","A","B","A"],
                   "销售额": [100,200,150,300,120]})
result = df.groupby("部门")["销售额"].sum().reset_index()
print(result)
```

## 常用聚合函数

sum(), mean(), count(), max(), min(), std()

## 你的任务

按"部门"分组, 计算每组"销售额"的总和, 打印分组结果.

预期输出: 分组求和后的 DataFrame
