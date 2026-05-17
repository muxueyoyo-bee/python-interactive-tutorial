import numpy as np
np.random.seed(42)

# 模拟: 真实函数 y=2x+1, 加噪声
X = np.linspace(0, 5, 20)
y_true = 2*X + 1 + np.random.randn(20)*0.5

# 模型1: 常数(高偏差)  model2: 过拟合(高方差)  model3: 刚好
m1 = np.full_like(X, np.mean(y_true))
m2 = np.polyval(np.polyfit(X, y_true, 10), X)  # 10次多项式
m3 = np.polyval(np.polyfit(X, y_true, 1), X)   # 1次(线性)

print("高偏差(欠拟合)误差:", round(np.mean((y_true-m1)**2), 3))
print("高方差(过拟合)误差:", round(np.mean((y_true-m2)**2), 3))
print("恰好拟合误差:     ", round(np.mean((y_true-m3)**2), 3))
