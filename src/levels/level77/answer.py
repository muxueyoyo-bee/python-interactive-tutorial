import numpy as np
np.random.seed(42)

def relu(x):
    return np.maximum(0, x)

def mlp_forward(X, W1, b1, W2, b2):
    h = relu(X @ W1 + b1)
    return h @ W2 + b2

X = np.array([[1, 2], [3, 4], [5, 6]])
W1 = np.random.randn(2, 4) * 0.1
b1 = np.zeros(4)
W2 = np.random.randn(4, 1) * 0.1
b2 = np.zeros(1)
out = mlp_forward(X, W1, b1, W2, b2)
print("输出形状:", out.shape)
print("输出值:", out.flatten().round(3))
