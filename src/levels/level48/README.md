# 第四十八关: 逻辑回归 - 分类入门

逻辑回归虽叫"回归", 实际上用于分类. 核心是 sigmoid 函数.

## Sigmoid 函数

sigma(z) = 1 / (1 + e^(-z)), 将任意实数压缩到 (0,1) 区间.

```python
import numpy as np
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

print(sigmoid(0))    # 0.5
print(sigmoid(2))    # 接近1
print(sigmoid(-2))   # 接近0
```

## 为什么用 sigmoid?

- 输出可解释为概率
- 在 z=0 附近近似线性
- 远离0时饱和, 防止极端值

## 你的任务

实现 sigmoid 函数, 分别计算 z=0, z=2, z=-2 时的值(保留3位小数).

预期输出:
```
sigmoid(0) = 0.5
sigmoid(2) = 0.881
sigmoid(-2) = 0.119
```
