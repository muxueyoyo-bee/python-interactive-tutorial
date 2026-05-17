import pandas as pd
data = {"姓名": ["张三", "李四", "王五"], "年龄": [25, 30, 28], "分数": [88, 92, 85]}
df = pd.DataFrame(data)
print(df)
print(df.describe())
