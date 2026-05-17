import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level71",
  title: "模型调参 — GridSearchCV",
  category: "搭建模型",
  description: "自动搜索SVM的最佳超参数",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 4,
  compareMode: "stdout",
  tags: ['调参', 'GridSearchCV'],
};

export default level;
