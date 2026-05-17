import numpy as np
np.random.seed(42)
Q = np.random.randn(4, 3)
K = np.random.randn(4, 3)
V = np.random.randn(4, 3)
d_k = 3
scores = Q @ K.T / np.sqrt(d_k)
print("娉ㄦ剰鍔涘垎鏁扮煩闃靛舰鐘?", scores.shape)
print("鍘熷鍒嗘暟(绗竴琛?:", np.round(scores[0], 2))
