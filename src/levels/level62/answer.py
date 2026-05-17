import numpy as np
np.random.seed(42)
def softmax(x):
    e = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return e / np.sum(e, axis=-1, keepdims=True)

def cross_attention(Q_dec, K_enc, V_enc, d_k):
    scores = Q_dec @ K_enc.T / np.sqrt(d_k)
    return softmax(scores) @ V_enc

enc_out = np.random.randn(5, 4)
dec_in = np.random.randn(3, 4)
result = cross_attention(dec_in, enc_out, enc_out, 4)
print("Cross-Attention 输出形状:", result.shape)
print("Decoder 关注 Encoder 的输出")
