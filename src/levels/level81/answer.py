from sklearn.datasets import make_blobs
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import numpy as np

X, y = make_blobs(n_samples=200, centers=2, random_state=42, cluster_std=1.2)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 绾挎€ф牳 vs RBF鏍?
for kernel in ["linear", "rbf"]:
    svm = SVC(kernel=kernel)
    svm.fit(X_train, y_train)
    print(f"SVM({kernel}): {svm.score(X_test, y_test):.2%}")
