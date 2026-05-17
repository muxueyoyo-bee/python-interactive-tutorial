# 第五十二关: K-Means 聚类

K-Means 是无监督学习算法, 将数据分成 K 个簇.

## 核心思想

1. 选 K 个初始中心点
2. 分配每个点到最近的中心
3. 重新计算每个簇的中心
4. 重复步骤2-3直到稳定

```python
import numpy as np
# 用欧氏距离找最近中心
centers = np.array([[1, 2], [8, 2], [5, 8]])
data = np.array([[1, 2], [5, 8], [8, 2], [9, 11]])
distances = np.linalg.norm(data[:, None] - centers[None, :], axis=2)
labels = np.argmin(distances, axis=1)
```

## 你的任务

对9个数据点用3个中心点做聚类, 打印每个点所属的簇标签.

预期输出: 每个数据点的簇标签数组
