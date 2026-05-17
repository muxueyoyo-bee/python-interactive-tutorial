import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level66",
  title: "scikit-learn 快速入门",
  category: "搭建模型",
  description: "使用sklearn完成第一个分类任务",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 2,
  compareMode: "stdout",
  tags: ['scikit-learn', '入门'],
};

export default level;
