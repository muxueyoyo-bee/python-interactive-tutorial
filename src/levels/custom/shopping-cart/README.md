# OOP实战: 购物车结算系统

> 涉及主线知识: 第26关 类与对象, 第8关 字典, 第14关 函数

## 场景

设计一个电商购物车的核心逻辑。用户添加商品后, 系统要能计算每个商品的小计和总价。

## 面向对象设计

```python
class ShoppingCart:
    def __init__(self):
        self.items = {}    # 商品名 -> 金额

    def add(self, name, price, qty=1):
        # 同名商品累加金额
        self.items[name] = self.items.get(name, 0) + price * qty
```

## 关键: dict.get() 的妙用

```python
self.items.get(name, 0)  # 如果name已存在返回金额, 否则返回0
```

> 回顾第8关: get()比[]安全, 键不存在时返回默认值而非报错。

## 你的任务

实现 ShoppingCart 类: add()方法支持商品名/单价/数量, receipt()方法打印每个商品金额和总合计。测试: Python入门(59元x2) + 算法导论(89元x1) + 键盘(299元x1)。
