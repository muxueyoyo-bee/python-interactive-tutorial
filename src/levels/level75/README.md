# 第七十五关: 综合AI实战 - 端到端项目

完整的机器学习项目流程.

## 标准流程

1. 加载数据 (load_breast_cancer)
2. 数据划分 (train_test_split)
3. 预处理 (StandardScaler)
4. 交叉验证评估 (cross_val_score)
5. 模型训练 (RandomForest)
6. 测试集验证
7. 特征重要性分析

```python
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score

# 全流程贯通
data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(...)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model = RandomForestClassifier(n_estimators=100, max_depth=5)
scores = cross_val_score(model, X_train, y_train, cv=5)
model.fit(X_train, y_train)
```

## 你的任务

完成一个端到端乳腺癌分类项目: 交叉验证 -> 测试集评估 -> 特征重要性.

预期输出: 交叉验证分数 + 测试准确率 + Top-3特征索引
