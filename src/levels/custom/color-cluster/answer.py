import numpy as np
from sklearn.cluster import KMeans
np.random.seed(42)

# 妯℃嫙鍥剧墖鍍忕礌: 200涓儚绱? RGB 3閫氶亾
pixels = np.random.randint(0, 256, (200, 3))

# 鑱氭垚5绉嶄富鑹茶皟
kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
kmeans.fit(pixels)
colors = kmeans.cluster_centers_.astype(int)
labels = kmeans.labels_

print("5绉嶄富鑹茶皟 (RGB):")
for i, c in enumerate(colors):
    count = np.sum(labels == i)
    print(f"  鑹茶皟{i+1}: RGB({c[0]},{c[1]},{c[2]}) - {count}鍍忕礌 ({count/len(pixels):.0%})")
