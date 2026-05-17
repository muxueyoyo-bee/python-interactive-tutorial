# 第七十二关: 特征工程

好的特征比复杂的模型更重要. SelectKBest 选出最相关的 K 个特征.

## 特征选择

```python
from sklearn.feature_selection import SelectKBest, f_classif

selector = SelectKBest(f_classif, k=5)
X_selected = selector.fit_transform(X, y)
```

## f_classif

方差分析 F 检验: 评估每个特征与标签的统计相关性, 分数越高越相关.

## 你的任务

从10个特征中选出最相关的5个, 打印原始特征数和选择后的特征数.

预期输出: 特征选择前后的维度对比 + Top-5特征索引
