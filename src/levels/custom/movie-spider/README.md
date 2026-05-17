# 数据实战: 电影评分分析

> 涉及主线知识: 第39关 DataFrame, 第12关 for循环

## 场景

你是某影评网站的数据分析师。主编让你从6部春节档电影的数据中找出评分最高的Top-3。

## DataFrame排序

```python
import pandas as pd
df = pd.DataFrame({...})
top = df.sort_values("评分", ascending=False).head(3)
```

sort_values 按指定列排序, head(n) 取前n行。ascending=False 表示降序(高分在前)。

## "性价比"指标

票房/评分: 衡量每分评分对应多少亿票房。高分低票房 = "叫好不叫座"。

```python
df["性价比"] = df["票房"] / df["评分"]
```

> 回顾第39关: DataFrame 可以直接创建计算列, pandas 自动广播运算。

## 你的任务

创建6部电影DataFrame, 计算评分Top-3, 打印电影名/评分/票房(不打印索引)。
