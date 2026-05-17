# 第四十九关: 梯度下降

梯度下降是机器学习的核心优化算法. 想象你站在山上想下山: 每一步往最陡的方向走.

## 数学原理

x_new = x_old - learning_rate * gradient

```python
def gradient_descent(lr=0.1, epochs=10):
    x = 10.0
    for _ in range(epochs):
        grad = 2 * x      # f(x)=x^2 的梯度
        x -= lr * grad
    return x
```

## 学习率的影响

- 太小: 收敛慢
- 太大: 可能震荡或发散
- 合适: 快速稳定收敛

## 你的任务

实现梯度下降, 从 x=10 开始, 学习率0.1, 迭代10次. 打印每次迭代后的 x 值.

预期输出: 逐渐趋近于0的一系列数值
