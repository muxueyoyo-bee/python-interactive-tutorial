import numpy as np
np.random.seed(42)
Q = np.random.randn(4, 3)
K = np.random.randn(4, 3)
V = np.random.randn(4, 3)
d_k = 3
scores = Q @ K.T / np.sqrt(d_k)
print("注意力分数矩阵形状:", scores.shape)
print("原始分数(第一行):", np.round(scores[0], 2))
