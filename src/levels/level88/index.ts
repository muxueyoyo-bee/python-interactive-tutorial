import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level88",
  title: "神经网络训练全流程",
  category: "AI进阶",
  description: "掌握神经网络训练全流程的核心概念与实现",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 5,
  compareMode: "stdout",
  tags: ['神经网络', '训练', 'numpy'],
};

export default level;
