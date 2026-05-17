# 第六十九关: 回归模型实战

线性回归 vs Ridge回归.

## Ridge 回归

在损失函数中加入 L2 惩罚: loss + alpha * sum(w^2)

防止系数过大, 提高泛化能力.

## R^2 (决定系数)

衡量模型解释了多少变异性: 越接近1越好, 0表示和瞎猜一样.

```python
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.model_selection import cross_val_score

lr = LinearRegression()
ridge = Ridge(alpha=1.0)
scores_lr = cross_val_score(lr, X, y, cv=5, scoring="r2")
scores_ridge = cross_val_score(ridge, X, y, cv=5, scoring="r2")
```

## 你的任务

对比 LinearRegression 和 Ridge 的 R2 分数.

预期输出: 两个模型的 R2 对比
