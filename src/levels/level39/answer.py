import pandas as pd
data = {"濮撳悕": ["寮犱笁", "鏉庡洓", "鐜嬩簲"], "骞撮緞": [25, 30, 28], "鍒嗘暟": [88, 92, 85]}
df = pd.DataFrame(data)
print(df)
print(df.describe())
