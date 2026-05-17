import pandas as pd
df = pd.DataFrame({"閮ㄩ棬": ["A", "B", "A", "B", "A"], "閿€鍞": [100, 200, 150, 300, 120]})
result = df.groupby("閮ㄩ棬")["閿€鍞"].sum().reset_index()
print(result)
