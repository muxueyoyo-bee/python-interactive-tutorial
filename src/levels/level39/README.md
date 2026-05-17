# 第三十九关: pandas DataFrame

DataFrame 是 Pandas 的二维数据表 -- 类似 Excel 表格或 SQL 表.

## 创建 DataFrame

```python
import pandas as pd
data = {"姓名": ["张三", "李四", "王五"],
        "年龄": [25, 30, 28],
        "分数": [88, 92, 85]}
df = pd.DataFrame(data)
print(df)
```

## 基本操作

```python
print(df.head(2))       # 前2行
print(df.describe())    # 数值列的统计摘要
print(df["分数"].mean())  # 某列的平均值
```

## 你的任务

创建一个包含"姓名"/"年龄"/"分数"三列的 DataFrame(三条记录), 打印整个 DataFrame 和 describe().

预期输出: DataFrame 表格 + describe() 统计
