# 第八十五关: 机器学习 Pipeline

> 前置回顾: 第67关 数据预处理(StandardScaler), 第81关 SVM, 第71关 GridSearchCV

## 为什么要Pipeline?

手动流程:
```python
X_train = scaler.fit_transform(X_train)  # 容易忘记对测试集也做!
X_test = scaler.transform(X_test)
model.fit(X_train, y_train)
```

Pipeline 一条龙:
```python
pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("svm", SVC())
])
pipe.fit(X_train, y_train)   # 自动先缩放再训练
pipe.score(X_test, y_test)   # 自动先缩放再预测
```

## Pipeline 的好处

1. **防止数据泄露**: 自动确保测试集只用训练集的统计量
2. **简洁**: 一个对象包含所有步骤
3. **可组合**: Pipeline 可以和 GridSearchCV 组合, 同时调多个步骤的参数

## 典型Pipeline

```python
# 分类Pipeline
Pipeline([
    ("scaler", StandardScaler()),      # 标准化
    ("poly", PolynomialFeatures()),     # 特征扩展
    ("selector", SelectKBest()),        # 特征选择
    ("classifier", RandomForest())      # 分类器
])

# 所有步骤一起交叉验证!
cross_val_score(pipe, X, y, cv=5)
```

> 回顾第67关: 手动写法需要记住 fit_transform vs transform 的区别。Pipeline 自动处理。

## 你的任务

创建 StandardScaler + SVC 的Pipeline, 在乳腺癌数据上训练并评估。

预期输出:
```
Pipeline测试准确率: xx%
Pipeline步骤: ['scaler', 'svm']
```
