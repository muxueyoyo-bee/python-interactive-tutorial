## # 第十二关: for 循环
for 循环用于遍历一个序列(列表, 字符串, 范围等)中的每个元素.

## range() 函数

range() 是 for 循环最常用的搭档, 用于生成数字序列:

```python
range(5)        # 0, 1, 2, 3, 4
range(1, 6)     # 1, 2, 3, 4, 5
range(1, 10, 2) # 1, 3, 5, 7, 9 (步长为2)
```

## 累加求和

```python
total = 0
for i in range(1, 11):
    total += i        # 等价于 total = total + i
print(total)          # 55
```

## 你的任务

用 for 循环计算 1+2+...+10 的和并打印.

预期输出:
```
55
```

