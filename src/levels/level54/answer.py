import numpy as np
def entropy(labels):
    _, counts = np.unique(labels, return_counts=True)
    probs = counts / len(labels)
    return -np.sum(probs * np.log2(probs))

labels = np.array([0, 0, 0, 1, 1, 1])
print(f"初始熵: {entropy(labels):.3f}")
left = np.array([0, 0, 0])
right = np.array([1, 1, 1])
info_gain = entropy(labels) - (3/6*entropy(left) + 3/6*entropy(right))
print(f"信息增益: {info_gain:.3f}")
