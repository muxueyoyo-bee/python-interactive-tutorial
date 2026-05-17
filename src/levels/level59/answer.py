import numpy as np
def positional_encoding(seq_len, d_model):
    pe = np.zeros((seq_len, d_model))
    for pos in range(seq_len):
        for i in range(0, d_model, 2):
            pe[pos, i] = np.sin(pos / (10000 ** (i/d_model)))
            if i+1 < d_model:
                pe[pos, i+1] = np.cos(pos / (10000 ** (i/d_model)))
    return pe

pe = positional_encoding(5, 8)
print("位置编码形状:", pe.shape)
print("第一位的前4维:", np.round(pe[0, :4], 3))
