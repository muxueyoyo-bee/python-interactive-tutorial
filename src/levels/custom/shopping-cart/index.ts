import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "shopping-cart",
  title: "购物车结算系统",
  category: "实战",
  description: "用类实现购物车加商品和结算",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '设计一个 ShoppingCart 类, 支持 add(商品,单价,数量) 和 receipt() 打印小票。商品: P...',
  type: "custom",
  difficulty: 3,
  compareMode: "stdout",
  tags: ['字典', '函数', 'OOP'],
};

export default level;
