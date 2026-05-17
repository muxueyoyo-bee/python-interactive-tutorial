from sklearn.datasets import make_classification
from sklearn.feature_selection import SelectKBest, f_classif
import numpy as np

X, y = make_classification(n_samples=200, n_features=10, n_informative=5, random_state=42)
selector = SelectKBest(f_classif, k=5)
X_selected = selector.fit_transform(X, y)
selected_idx = np.argsort(selector.scores_)[-5:]
print(f"鍘熷鐗瑰緛鏁? {X.shape[1]}")
print(f"閫夋嫨鐗瑰緛鏁? {X_selected.shape[1]}")
print(f"Top-5 鐗瑰緛绱㈠紩: {sorted(selected_idx)}")
