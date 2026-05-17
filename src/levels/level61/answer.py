import numpy as np
np.random.seed(42)

def softmax(x, axis=-1):
    e = np.exp(x - np.max(x, axis=axis, keepdims=True))
    return e / np.sum(e, axis=axis, keepdims=True)

def self_attention(Q, K, V, d_k):
    scores = Q @ K.T / np.sqrt(d_k)
    return softmax(scores) @ V

def layer_norm(x, eps=1e-5):
    mean, var = np.mean(x, axis=-1, keepdims=True), np.var(x, axis=-1, keepdims=True)
    return (x - mean) / np.sqrt(var + eps)

def encoder_layer(x, d_model=4, d_ff=8):
    attn_out = self_attention(x, x, x, d_model)
    x = layer_norm(x + attn_out)
    W1, W2 = np.random.randn(d_model, d_ff)*0.1, np.random.randn(d_ff, d_model)*0.1
    ff_out = np.maximum(0, x @ W1) @ W2
    return layer_norm(x + ff_out)

x = np.random.randn(3, 4)
out = encoder_layer(x)
print("Encoder 杈撳嚭褰㈢姸:", out.shape)
