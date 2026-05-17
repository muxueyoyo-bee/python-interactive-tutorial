import numpy as np
np.random.seed(42)
def layer_norm(x, eps=1e-5):
    mean = np.mean(x, axis=-1, keepdims=True)
    var = np.var(x, axis=-1, keepdims=True)
    return (x - mean) / np.sqrt(var + eps)

def feed_forward(x, d_ff=8):
    W1 = np.random.randn(x.shape[1], d_ff) * 0.1
    W2 = np.random.randn(d_ff, x.shape[1]) * 0.1
    return np.maximum(0, x @ W1) @ W2

x = np.random.randn(3, 4)
out = feed_forward(x)
print("鍓嶉缃戠粶杈撳嚭褰㈢姸:", out.shape)
print("LayerNorm 鍚庡潎鍊尖増0:", round(float(np.mean(layer_norm(out))), 5))
