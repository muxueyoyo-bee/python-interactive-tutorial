import numpy as np
w = np.array([0.5, -2.1, 3.7, 0.3, -1.5])
l1 = np.sum(np.abs(w))
l2 = np.sum(w ** 2)
print(f"L1 姝ｅ垯鍖栭」: {l1:.2f}")
print(f"L2 姝ｅ垯鍖栭」: {l2:.2f}")
