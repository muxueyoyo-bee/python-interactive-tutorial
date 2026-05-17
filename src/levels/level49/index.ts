import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level49",
  title: "梯度下降 — 模型如何学习",
  category: "AI基础",
  description: "手写梯度下降优化器，理解模型参数如何更新",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 3,
  compareMode: "stdout",
  tags: ['梯度下降', '优化', 'numpy'],
};

export default level;
