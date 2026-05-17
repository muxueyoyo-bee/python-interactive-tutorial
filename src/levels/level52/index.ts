import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level52",
  title: "K-Means 聚类",
  category: "AI基础",
  description: "用numpy实现K-Means算法核心步骤",
  content: "",
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 3,
  compareMode: "stdout",
  tags: ['K-Means', '聚类', 'numpy'],
};

export default level;
