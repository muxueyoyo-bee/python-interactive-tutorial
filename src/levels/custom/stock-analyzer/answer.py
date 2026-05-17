import pandas as pd
import numpy as np
np.random.seed(42)
dates = pd.date_range('2025-01-01', periods=20)
df = pd.DataFrame({'close': np.cumsum(np.random.randn(20)) + 100})
df['ma5'] = df['close'].rolling(5).mean()
df['ma10'] = df['close'].rolling(10).mean()
print(df[['close','ma5','ma10']].dropna().round(2))
