import numpy as np
np.random.seed(42)
data = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11], [8, 2], [10, 2], [9, 3]])
centers = np.array([[1, 2], [8, 2], [5, 8]])
labels = np.argmin(np.linalg.norm(data[:, None] - centers[None, :], axis=2), axis=1)
print(labels)
