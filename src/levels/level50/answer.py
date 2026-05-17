import numpy as np
y_true = np.array([3, 5, 2, 8])
y_pred = np.array([2.5, 5.5, 2.2, 7.5])
mse = np.mean((y_true - y_pred) ** 2)
mae = np.mean(np.abs(y_true - y_pred))
print(f"MSE: {mse:.3f}")
print(f"MAE: {mae:.3f}")
