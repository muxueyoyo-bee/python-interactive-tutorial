import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level43",
  title: "matplotlib 折线图",
  category: "数据分析",
  description: "绘制基本折线图",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 4,
  compareMode: "plot",
  tags: ['matplotlib', '折线图'],
};

export default level;
