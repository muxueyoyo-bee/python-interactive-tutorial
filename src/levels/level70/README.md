# 第七十关: 聚类分析实战

## KMeans + 轮廓系数

轮廓系数(Silhouette Score)衡量聚类质量:
- 值在 [-1, 1] 之间
- 越大表示簇内紧凑, 簇间分离

```python
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

model = KMeans(n_clusters=3, n_init=10)
labels = model.fit_predict(X)
print(f"轮廓系数: {silhouette_score(X, labels):.3f}")
```

## 如何选 K?

尝试不同的 K 值, 选轮廓系数最大的.

## 你的任务

用 KMeans(n=3) 聚类, 计算并打印轮廓系数.

预期输出: 轮廓系数 + 聚类中心数
