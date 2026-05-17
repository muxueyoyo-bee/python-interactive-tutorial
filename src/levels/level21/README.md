# 第二十一关: 文件写入

使用 open() 的写入模式将数据保存到文件.

## 写入文件

```python
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello\n")
```

## 写入多行

```python
lines = ["第一行", "第二行", "第三行"]
content = "\n".join(lines)  # 用换行符连接
print(content)
```

> "\n".join(list) 用换行符连接列表中的所有元素.

## 你的任务

将三行文字用换行符连接后打印(模拟文件写入的结果).

预期输出:
```
第一行
第二行
第三行
```
