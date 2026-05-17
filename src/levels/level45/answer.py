import pandas as pd
import numpy as np
np.random.seed(42)
df = pd.DataFrame({"month": range(1, 13), "sales": np.random.randint(100, 500, 12)})
result = {"total": int(df["sales"].sum()), "avg": round(float(df["sales"].mean()), 1), "max_month": int(df.loc[df["sales"].idxmax(), "month"])}
print(result)
