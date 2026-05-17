import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "shopping-cart",
  title: "购物车结算系统",
  category: "实战",
  description: "用类实现购物车加商品和结算",
  content: md,
  defaultCode: 'class ShoppingCart:\n    def __init__(self):\n        self.items = {}\n\n    def add(self, name, price, qty=1):\n        # 同名商品累加金额到 self.items[name]\n        pass\n\n    def total(self):\n        # 返回所有商品的金额总和\n        pass\n\n    def receipt(self):\n        # 打印每个商品名: 金额, 最后打印 合计: xxx 元\n        pass\n\n# 创建购物车, 添加: Python入门(59)x2, 算法导论(89)x1, 键盘(299)x1\n# 调用 cart.receipt() 打印小票',
  answer,
  hint: '设计一个 ShoppingCart 类, 支持 add(商品,单价,数量) 和 receipt() 打印小票。商品: P...',
  type: "custom",
  difficulty: 3,
  compareMode: "stdout",
  tags: ['字典', '函数', 'OOP'],
};

export default level;
