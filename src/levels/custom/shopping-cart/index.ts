import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "shopping-cart",
  title: "购物车结算系统",
  category: "实战",
  description: "用类实现购物车加商品和结算",
  content: md,
  defaultCode: 'class ShoppingCart:\n    def __init__(self):\n        self.items = {}\n\n    def add(self, name, price, qty=1):\n        # TODO: 同名商品累加金额\n        pass\n\n    def total(self):\n        # TODO: 返回总金额\n        pass\n\n    def receipt(self):\n        # TODO: 打印每个商品金额 + 合计\n        pass\n\n# TODO: 创建cart实例, 添加3个商品, 调用cart.receipt()\n',
  answer,
  hint: '设计一个 ShoppingCart 类, 支持 add(商品,单价,数量) 和 receipt() 打印小票。商品: P...',
  type: "custom",
  difficulty: 3,
  compareMode: "stdout",
  tags: ['字典', '函数', 'OOP'],
};

export default level;
