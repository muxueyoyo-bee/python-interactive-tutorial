import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level44",
  title: "matplotlib 柱状图",
  category: "数据分析",
  description: "绘制柱状图",
  content: "",
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 4,
  compareMode: "plot",
  tags: ['matplotlib', '柱状图'],
};

export default level;
