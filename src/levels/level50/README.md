# 第五十关: 损失函数

损失函数衡量模型预测与真实值的差距. 损失越小, 模型越好.

## MSE (均方误差)

MSE = average((y_pred - y_true)^2), 对大误差惩罚更重.

## MAE (平均绝对误差)

MAE = average(|y_pred - y_true|), 对异常值更鲁棒.

```python
import numpy as np
y_true = np.array([3, 5, 2, 8])
y_pred = np.array([2.5, 5.5, 2.2, 7.5])
mse = np.mean((y_true - y_pred) ** 2)
mae = np.mean(np.abs(y_true - y_pred))
```

## 你的任务

计算给定真实值和预测值的 MSE 和 MAE (都保留3位小数).

预期输出:
```
MSE: 0.135
MAE: 0.325
```
