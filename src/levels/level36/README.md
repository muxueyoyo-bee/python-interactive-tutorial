# 第三十六关: numpy 基础 - 创建数组

NumPy 是 Python 科学计算的基础. ndarray(N维数组)是其核心.

## 创建数组

```python
import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(a)            # [1 2 3 4 5]
print(a.shape)      # (5,)     -- 形状
print(a.dtype)      # int32    -- 数据类型
```

## 数组属性

| 属性 | 含义 |
|------|------|
| .shape | 数组的形状 |
| .dtype | 元素的数据类型 |
| .ndim | 维数 |
| .size | 元素总数 |

## 你的任务

创建 numpy 数组 [1, 2, 3, 4, 5], 打印数组内容, 形状和数据类型.

预期输出:
```
[1 2 3 4 5]
(5,)
int32
```
