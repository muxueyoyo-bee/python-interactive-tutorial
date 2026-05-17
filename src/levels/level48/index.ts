import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level48",
  title: "逻辑回归 — 分类入门",
  category: "AI基础",
  description: "实现sigmoid函数，理解分类问题的核心激活函数",
  content: "",
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 3,
  compareMode: "stdout",
  tags: ['逻辑回归', 'numpy', 'sigmoid'],
};

export default level;
