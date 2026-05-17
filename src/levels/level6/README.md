# 第六关: 列表的增删改查

> 前置回顾: 第5关 列表的创建和索引

## Create: 增加元素

```python
nums = [1, 2, 3]

nums.append(4)         # 末尾追加 -> [1, 2, 3, 4]
nums.insert(0, 0)      # 指定位置插入 -> [0, 1, 2, 3, 4]
```

## Delete: 删除元素

```python
nums = [1, 2, 3, 2]

nums.remove(2)         # 删除第一个值为2的元素
nums.pop()             # 弹出最后一个
nums.pop(0)            # 弹出索引0的元素
```

## Update: 修改元素

```python
nums = [1, 2, 3]
nums[0] = 99           # [99, 2, 3]
```

> 回顾: 这和变量赋值一样 -- `=` 把右边的值放到左边指定的位置。

## append vs insert

```python
nums = [1, 2, 3]
nums.append(4)      # 加到最后 -> [1,2,3,4]
nums.insert(0, 0)   # 加到最前 -> [0,1,2,3,4]
```

append 不需要指定位置, insert 需要。append 更常用。

## 常见错误

- `nums.append([4,5])` 会把整个列表作为一个元素: `[1,2,3,[4,5]]`
- `nums.remove(99)` 当 99 不在列表中时报 ValueError

## 你的任务

从 [1,2,3] 开始: append(4) -> insert(0,0) -> remove(2) -> 打印最终列表。

预期输出:
```
[0, 1, 3, 4]
```
