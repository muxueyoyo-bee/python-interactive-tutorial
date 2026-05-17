# 第八十七关: 特征缩放 -- 标准化 vs 归一化

> 前置回顾: 第67关 StandardScaler, 第85关 Pipeline

## 为什么需要缩放?

年龄(0-100)和收入(0-100000)量纲差1000倍, 距离-based模型(SVM, KNN, K-Means)会被大数值特征主导。

## 三种缩放器

```python
# 1. StandardScaler: (x - mean) / std -> 均0方1
#    适合: 大多数情况, 假设正态分布

# 2. MinMaxScaler: (x - min) / (max - min) -> [0, 1]
#    适合: 已知边界, 需要保留稀疏性

# 3. RobustScaler: (x - median) / IQR
#    适合: 有异常值, 用中位数和四分位距
```

## 选哪个?

| 情况 | 推荐 |
|------|------|
| 正态分布数据 | StandardScaler |
| 神经网络 | StandardScaler 或 MinMax |
| 大量异常值 | RobustScaler |
| 图像像素 | 除以255 |
| 文本TF-IDF | 不需要额外缩放 |

> 重点: 只在训练集上 fit, 测试集用 transform。Pipeline(第85关)可以自动保证这一点。

## 你的任务

对年龄+收入数据, 对比 Standard, MinMax, Robust 三种缩放后的均值和标准差。

预期输出:
```
Standard: mean=[0 0], std=[1 1]
MinMax: mean=[xxx], std=[xxx]
Robust: mean=[xxx], std=[xxx]
```
