import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level81",
  title: "SVM: 最大间隔分类器",
  category: "AI进阶",
  description: "掌握SVM: 最大间隔分类器的核心概念与实现",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 4,
  compareMode: "stdout",
  tags: ['SVM', '核方法', 'sklearn'],
};

export default level;
