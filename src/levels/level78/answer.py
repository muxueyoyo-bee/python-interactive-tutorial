import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

# 简单网络: x -> w -> y_pred, loss = (y_pred - y_true)^2
x = 0.5
w = 0.8
y_true = 1.0

# 前向
y_pred = sigmoid(w * x)
loss = (y_pred - y_true)**2

# 反向: dL/dw = dL/dy_pred * dy_pred/dz * dz/dw
dL_dy = 2 * (y_pred - y_true)
dy_dz = y_pred * (1 - y_pred)  # sigmoid导数
dz_dw = x
grad = dL_dy * dy_dz * dz_dw

print(f"预测: {y_pred:.3f}")
print(f"损失: {loss:.4f}")
print(f"梯度 dL/dw: {grad:.4f}")
