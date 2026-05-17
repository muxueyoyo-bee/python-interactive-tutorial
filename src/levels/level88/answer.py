import numpy as np
np.random.seed(42)

def sigmoid(x): return 1/(1+np.exp(-x))
def mse(y, t): return np.mean((y-t)**2)

# 玩具数据: XOR
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

# 1隐藏层网络
n_hidden = 3
W1 = np.random.randn(2, n_hidden) * 0.5
b1 = np.zeros(n_hidden)
W2 = np.random.randn(n_hidden, 1) * 0.5
b2 = np.zeros(1)
lr = 0.5

for epoch in range(2000):
    # Forward
    h = sigmoid(X @ W1 + b1)
    out = sigmoid(h @ W2 + b2)
    # Backward (简化)
    d_out = (out - y) * out * (1-out)
    d_h = d_out @ W2.T * h * (1-h)
    # Update
    W2 -= lr * h.T @ d_out
    b2 -= lr * d_out.sum(axis=0)
    W1 -= lr * X.T @ d_h
    b1 -= lr * d_h.sum(axis=0)

print(f"XOR网络训练2000轮后损失: {mse(out, y):.4f}")
print(f"预测: {out.flatten().round(2)}")
