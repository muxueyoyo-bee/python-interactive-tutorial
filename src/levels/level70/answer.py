from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

X, y_true = make_blobs(n_samples=200, centers=3, random_state=42, cluster_std=1.5)
model = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = model.fit_predict(X)
print(f"轮廓系数: {silhouette_score(X, labels):.3f}")
print(f"聚类中心数: {model.n_clusters}")
