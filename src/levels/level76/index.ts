import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level76",
  title: "感知机: 神经网络的原子",
  category: "AI进阶",
  description: "掌握感知机: 神经网络的原子的核心概念与实现",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 3,
  compareMode: "stdout",
  tags: ['感知机', '神经网络', 'numpy'],
};

export default level;
