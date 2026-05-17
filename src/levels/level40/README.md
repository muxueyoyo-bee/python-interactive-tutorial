# 第四十关: pandas 读取 CSV

CSV(逗号分隔值)是最通用的数据交换格式. Pandas 可以方便地读取和写入 CSV.

## 读取 CSV

```python
import pandas as pd
from io import StringIO

csv_data = "name,score\nAlice,85\nBob,92\nCharlie,78"
df = pd.read_csv(StringIO(csv_data))
print(df)
print(f"平均分: {df['score'].mean():.1f}")
```

常用参数: sep=','分隔符, encoding='utf-8'编码

## 你的任务

读取 CSV 数据(3条姓名+分数), 打印 DataFrame, 计算并打印平均分(保留1位小数).

预期输出: DataFrame + 平均分
