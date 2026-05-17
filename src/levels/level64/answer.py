import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(42)
words = ["鎴?, "鐖?, "Python", "缂栫▼"]
attn_weights = np.random.rand(4, 4)
attn_weights = attn_weights / attn_weights.sum(axis=1, keepdims=True)
fig, ax = plt.subplots(figsize=(6, 5))
im = ax.imshow(attn_weights, cmap="Blues", vmin=0, vmax=1)
ax.set_xticks(range(4))
ax.set_yticks(range(4))
ax.set_xticklabels(words, fontsize=10)
ax.set_yticklabels(words, fontsize=10)
ax.set_title("Self-Attention 鏉冮噸鍙鍖?, fontsize=12)
plt.colorbar(im)
plt.tight_layout()
plt.show()
