# 第五十三关: KNN - 最近邻分类

KNN 是最直观的分类算法: 找最近的 K 个邻居, 投票决定类别.

## 距离度量

欧氏距离: sqrt(sum((xi - yi)^2))

```python
import numpy as np
def knn_predict(x_new, X_train, y_train, k=3):
    dist = np.linalg.norm(X_train - x_new, axis=1)
    neighbors = y_train[np.argsort(dist)[:k]]
    return int(np.bincount(neighbors).argmax())
```

## 你的任务

实现 KNN (k=3), 对新数据点 [4,3] 预测类别.

预期输出:
```
0
```
