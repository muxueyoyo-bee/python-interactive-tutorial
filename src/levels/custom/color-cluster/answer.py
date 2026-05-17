import numpy as np
from sklearn.cluster import KMeans
np.random.seed(42)

# 模拟图片像素: 200个像素, RGB 3通道
pixels = np.random.randint(0, 256, (200, 3))

# 聚成5种主色调
kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
kmeans.fit(pixels)
colors = kmeans.cluster_centers_.astype(int)
labels = kmeans.labels_

print("5种主色调 (RGB):")
for i, c in enumerate(colors):
    count = np.sum(labels == i)
    print(f"  色调{i+1}: RGB({c[0]},{c[1]},{c[2]}) - {count}像素 ({count/len(pixels):.0%})")
