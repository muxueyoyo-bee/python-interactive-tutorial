import numpy as np
np.random.seed(42)
def multi_head_attention(Q, K, V, n_heads=2):
    d_model = Q.shape[1]
    d_k = d_model // n_heads
    outputs = []
    for h in range(n_heads):
        Wq = np.eye(d_model)[:, h*d_k:(h+1)*d_k]
        q_h, k_h, v_h = Q @ Wq, K @ Wq, V @ Wq
        scores = q_h @ k_h.T / np.sqrt(d_k)
        attn = np.exp(scores) / np.sum(np.exp(scores), axis=1, keepdims=True)
        outputs.append(attn @ v_h)
    return np.concatenate(outputs, axis=1)

x = np.random.randn(4, 4)
result = multi_head_attention(x, x, x, 2)
print("多头注意力输出形状:", result.shape)
