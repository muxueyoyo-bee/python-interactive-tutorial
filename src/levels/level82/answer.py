import numpy as np
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data  # 4缁寸壒寰?

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

print(f"鍘熷缁村害: {X.shape[1]}")
print(f"闄嶇淮鍚庣淮搴? {X_pca.shape[1]}")
print(f"淇濈暀鏂瑰樊姣? {pca.explained_variance_ratio_.round(3)}")
print(f"鎬讳繚鐣? {pca.explained_variance_ratio_.sum():.1%}")
