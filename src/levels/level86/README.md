# 第八十六关: 交叉验证深入

> 前置回顾: 第68关 分类模型对比(cross_val_score), 第71关 GridSearchCV

## 为什么需要交叉验证?

单次划分 train/test 有随机性 -- 运气好分到容易的测试集, 准确率虚高。交叉验证消除这种随机性。

## K-Fold vs Stratified K-Fold

```python
# 普通K-Fold: 随机分成K份
KFold(n_splits=5, shuffle=True)

# Stratified K-Fold: 保持每份的类别比例
StratifiedKFold(n_splits=5, shuffle=True)
```

| | K-Fold | Stratified |
|------|--------|------------|
| 类别比例 | 不保证 | 保证一致 |
| 适用 | 回归 | 分类(强烈推荐) |
| 小样本 | 可能有折没有某类 | 每折各类都有代表 |

## 交叉验证策略选择

- **分类**: 默认用 StratifiedKFold
- **回归**: 用 KFold
- **时间序列**: 用 TimeSeriesSplit (不能打乱顺序)
- **超大数据**: 2-3折就够了, 5-10折太慢

## 你的任务

对比 KFold 和 StratifiedKFold 在 digits 数据上的5折交叉验证结果。

预期输出:
```
KFold(5): 0.xxx +/- 0.xxx
Stratified(5): 0.xxx +/- 0.xxx
```
