# 第七十三关: 模型持久化

用 pickle 将训练好的模型保存为文件, 之后可以直接加载使用.

## 保存模型

```python
import pickle
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
```

## 加载模型

```python
with open("model.pkl", "rb") as f:
    loaded = pickle.load(f)
print(loaded.score(X_test, y_test))
```

## 你的任务

训练一个随机森林, 用 pickle 序列化到内存, 再加载回来, 验证准确率一致.

预期输出: 序列化前后准确率一致 + 序列化大小
