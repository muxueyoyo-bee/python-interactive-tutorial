import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level79",
  title: "激活函数全家桶",
  category: "AI进阶",
  description: "掌握激活函数全家桶的核心概念与实现",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 3,
  compareMode: "stdout",
  tags: ['激活函数', 'ReLU', 'sigmoid', 'tanh'],
};

export default level;
