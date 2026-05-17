import numpy as np
X = np.array([[1, 2], [2, 3], [3, 1], [6, 5], [7, 7], [8, 6]])
y = np.array([0, 0, 0, 1, 1, 1])
def knn_predict(x_new, k=3):
    dist = np.linalg.norm(X - x_new, axis=1)
    neighbors = y[np.argsort(dist)[:k]]
    return int(np.bincount(neighbors).argmax())

print(knn_predict(np.array([4, 3]), 3))
