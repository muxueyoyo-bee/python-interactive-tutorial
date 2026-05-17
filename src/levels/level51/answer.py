import numpy as np
w = np.array([0.5, -2.1, 3.7, 0.3, -1.5])
l1 = np.sum(np.abs(w))
l2 = np.sum(w ** 2)
print(f"L1 正则化项: {l1:.2f}")
print(f"L2 正则化项: {l2:.2f}")
