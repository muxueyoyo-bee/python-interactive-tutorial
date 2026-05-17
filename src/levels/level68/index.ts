import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level68",
  title: "分类模型实战 — 多种算法对比",
  category: "搭建模型",
  description: "对比逻辑回归、决策树、随机森林的性能",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 4,
  compareMode: "stdout",
  tags: ['分类', '对比'],
};

export default level;
