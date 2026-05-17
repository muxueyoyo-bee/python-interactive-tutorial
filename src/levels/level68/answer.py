from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import numpy as np

X, y = make_classification(n_samples=200, n_features=10, n_informative=5, random_state=42)
models = {"LR": LogisticRegression(max_iter=200), "DT": DecisionTreeClassifier(max_depth=5), "RF": RandomForestClassifier(n_estimators=50)}
for name, m in models.items():
    scores = cross_val_score(m, X, y, cv=5)
    print(f"{name}: {np.mean(scores):.2%} ± {np.std(scores):.2%}")
