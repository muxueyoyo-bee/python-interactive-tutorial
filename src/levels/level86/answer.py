from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, StratifiedKFold, KFold
import numpy as np

digits = load_digits()
X, y = digits.data[:500], digits.target[:500]
model = RandomForestClassifier(n_estimators=50, random_state=42)

for name, cv in [("KFold(5)", KFold(5, shuffle=True, random_state=42)),
                  ("Stratified(5)", StratifiedKFold(5, shuffle=True, random_state=42))]:
    scores = cross_val_score(model, X, y, cv=cv)
    print(f"{name}: {np.mean(scores):.3f} +/- {np.std(scores):.3f}")
