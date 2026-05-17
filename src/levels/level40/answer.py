import pandas as pd
from io import StringIO
csv_data = "name,score\nAlice,85\nBob,92\nCharlie,78"
df = pd.read_csv(StringIO(csv_data))
print(df)
print(f"平均分: {df["score"].mean():.1f}")
