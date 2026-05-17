import numpy as np
np.random.seed(42)
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
w = np.sum(X * y) / np.sum(X * X)
print(f"鎷熷悎鏂滅巼 w = {w:.2f}")
