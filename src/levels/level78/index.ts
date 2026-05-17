import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level78",
  title: "反向传播: 神经网络如何学习",
  category: "AI进阶",
  description: "掌握反向传播: 神经网络如何学习的核心概念与实现",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 5,
  compareMode: "stdout",
  tags: ['反向传播', '梯度', '链式法则'],
};

export default level;
