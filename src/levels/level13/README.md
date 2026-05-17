# 第十三关: while 循环

> 前置回顾: 第12关 for 用于"知道次数"的重复, while 用于"不知道确切次数"的重复

## for vs while

```python
# for: 你知道要遍历什么
for i in range(1, 11):
    print(i)

# while: 你只知道继续的条件
n = 1
while n <= 10:
    print(n)
    n += 1              # 关键: 必须有这行!
```

| 场景 | for | while |
|------|-----|-------|
| 遍历列表/range | 推荐 | 可以但非最佳 |
| 等待条件满足 | 不行 | 推荐 |
| 无限循环 | 不行 | `while True` |

## 死循环警告!

```python
# 这永远不会停! 浏览器会卡住!
n = 1
while n <= 10:
    print(n)
    # 忘了写 n += 1 -- 死循环!
```

> 在 Pyodide 浏览器里写死循环: 刷新页面即可恢复。

## 同题不同解

```python
# for 求和 (第12关)
total = 0
for i in range(1, 11):
    total += i

# while 求和 -- 同样结果, 不同写法
total = 0; n = 1
while n <= 10:
    total += n
    n += 1
```

for 更简洁, while 让你更清楚每一步在做什么。

## 常见错误

- 忘写自增: `n += 1` 忘了 -> 死循环
- 条件永远不成立 -> 循环体从不执行
- 自增缩进错误 -> 写在循环外面

## 你的任务

用 while 循环计算 1+2+...+10 的和并打印。

预期输出:
```
55
```
