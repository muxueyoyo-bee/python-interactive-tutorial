import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level70",
  title: "聚类分析实战",
  category: "搭建模型",
  description: "使用KMeans和轮廓系数评估聚类质量",
  content: "",
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 3,
  compareMode: "stdout",
  tags: ['聚类', 'KMeans', 'DBSCAN'],
};

export default level;
