import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level45",
  title: "综合数据分析实战",
  category: "数据分析",
  description: "综合运用pandas+numpy完成数据分析",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 5,
  compareMode: "both",
  tags: ['综合', 'pandas', 'matplotlib'],
};

export default level;
