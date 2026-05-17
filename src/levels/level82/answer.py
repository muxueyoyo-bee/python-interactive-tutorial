import numpy as np
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data  # 4维特征

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

print(f"原始维度: {X.shape[1]}")
print(f"降维后维度: {X_pca.shape[1]}")
print(f"保留方差比: {pca.explained_variance_ratio_.round(3)}")
print(f"总保留: {pca.explained_variance_ratio_.sum():.1%}")
