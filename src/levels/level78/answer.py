import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

# 绠€鍗曠綉缁? x -> w -> y_pred, loss = (y_pred - y_true)^2
x = 0.5
w = 0.8
y_true = 1.0

# 鍓嶅悜
y_pred = sigmoid(w * x)
loss = (y_pred - y_true)**2

# 鍙嶅悜: dL/dw = dL/dy_pred * dy_pred/dz * dz/dw
dL_dy = 2 * (y_pred - y_true)
dy_dz = y_pred * (1 - y_pred)  # sigmoid瀵兼暟
dz_dw = x
grad = dL_dy * dy_dz * dz_dw

print(f"棰勬祴: {y_pred:.3f}")
print(f"鎹熷け: {loss:.4f}")
print(f"姊害 dL/dw: {grad:.4f}")
