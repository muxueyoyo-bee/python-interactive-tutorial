import pandas as pd
df = pd.DataFrame({"部门": ["A", "B", "A", "B", "A"], "销售额": [100, 200, 150, 300, 120]})
result = df.groupby("部门")["销售额"].sum().reset_index()
print(result)
