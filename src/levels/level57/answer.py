import numpy as np
np.random.seed(42)
Q = np.random.randn(4, 3)
K = np.random.randn(4, 3)
V = np.random.randn(4, 3)
d_k = 3
scores = Q @ K.T / np.sqrt(d_k)
def softmax(x):
    e = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return e / np.sum(e, axis=-1, keepdims=True)

attn = softmax(scores)
output = attn @ V
print("注意力权重和为1:", np.allclose(attn.sum(axis=1), 1))
print("输出形状:", output.shape)
