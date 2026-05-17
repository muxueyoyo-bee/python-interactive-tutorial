import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level53",
  title: "KNN — 最近邻分类",
  category: "AI基础",
  description: "实现KNN分类算法，理解基于距离的学习",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 3,
  compareMode: "stdout",
  tags: ['KNN', '分类'],
};

export default level;
