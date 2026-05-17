import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level74",
  title: "小型文本分类项目",
  category: "搭建模型",
  description: "用朴素贝叶斯完成英文文本情感分类",
  content: "",
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 5,
  compareMode: "stdout",
  tags: ['文本分类', 'NLP', '项目'],
};

export default level;
