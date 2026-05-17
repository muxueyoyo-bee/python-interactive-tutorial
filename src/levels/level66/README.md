# 第六十六关: scikit-learn 快速入门

scikit-learn 是 Python 最流行的机器学习库, 提供统一的 fit/predict 接口.

## 三步走

```python
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# 1. 加载数据
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3)

# 2. 训练模型
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# 3. 评估
print(f"准确率: {model.score(X_test, y_test):.2%}")
```

## fit/predict/score

- fit(): 训练模型
- predict(): 预测新数据
- score(): 评估准确率

## 你的任务

用 KNN (k=3) 分类鸢尾花数据, 打印测试准确率.

预期输出:
```
测试准确率: 90%+
```
