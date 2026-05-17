import pandas as pd
left = pd.DataFrame({"id": [1, 2, 3], "name": ["Alice", "Bob", "Charlie"]})
right = pd.DataFrame({"id": [1, 2, 3], "score": [85, 92, 78]})
merged = pd.merge(left, right, on="id")
print(merged)
