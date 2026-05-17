# 第六十七关: 数据预处理实战

原始数据需要预处理才能输入模型.

## StandardScaler (标准化)

z = (x - mean) / std, 使特征均值为0, 方差为1.

```python
from sklearn.preprocessing import StandardScaler
import numpy as np

X = np.array([[25, 50000], [30, 80000], [35, 120000]])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

## 为什么标准化?

- 让不同量纲的特征公平比较
- 加速梯度下降收敛
- 对距离-based算法(如KNN, SVM)至关重要

## 你的任务

对3条数据(年龄+工资)做标准化, 打印原始数据和标准化后数据.

预期输出: 标准化前后对比
