from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import cross_val_score
import numpy as np

X, y = make_classification(n_samples=300, n_features=10, random_state=42)

for name, clf in [("RandomForest", RandomForestClassifier(n_estimators=100)),
                   ("GradientBoost", GradientBoostingClassifier(n_estimators=100))]:
    scores = cross_val_score(clf, X, y, cv=5)
    print(f"{name}: {np.mean(scores):.2%} +/- {np.std(scores):.2%}")
