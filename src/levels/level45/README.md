# 第四十五关: 综合数据分析实战

综合运用 pandas + numpy 完成一个完整的分析任务.

## 分析流程

典型的数据分析项目: 创建数据 -> 计算指标 -> 输出结果.

```python
import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({
    "month": range(1, 13),
    "sales": np.random.randint(100, 500, 12)
})

result = {
    "total": int(df["sales"].sum()),
    "avg": round(float(df["sales"].mean()), 1),
    "max_month": int(df.loc[df["sales"].idxmax(), "month"])
}
print(result)
```

## 你的任务

生成12个月的随机销售数据, 计算总销售额, 月均值, 最高月份, 输出为一个字典.

预期输出: 包含 total/avg/max_month 的字典
