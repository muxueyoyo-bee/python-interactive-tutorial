import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level46",
  title: "什么是人工智能",
  category: "AI基础",
  description: "理解人工智能(Artificial Intelligence)、机器学习(Machine Learning)、深度学习(Deep Learning)三者的关系",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 1,
  compareMode: "stdout",
  tags: ['AI', 'ML', 'DL', '入门'],
};

export default level;
