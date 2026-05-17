# 第三十五关: 单元测试

单元测试是验证代码正确性的基础方法. 最简单的测试工具是 assert 语句.

## assert 语句

```python
assert 条件, "失败时的提示信息"
```

条件为 True 时什么都不发生; 为 False 时抛出 AssertionError.

## 编写测试

```python
def add(a, b):
    return a + b

assert add(1, 2) == 3
assert add(-1, 1) == 0
assert add(0, 0) == 0

print("All tests passed!")
```

## TDD (测试驱动开发)

1. 先写测试 -> 2. 写代码让测试通过 -> 3. 重构优化

## 你的任务

定义 add(a, b) 函数, 用 assert 测试三个用例, 全部通过后打印 "All tests passed!".

预期输出:
```
All tests passed!
```
