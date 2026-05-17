import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level90",
  title: "端到端ML项目: 房价预测",
  category: "AI进阶",
  description: "掌握端到端ML项目: 房价预测的核心概念与实现",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 5,
  compareMode: "stdout",
  tags: ['端到端', '项目', '回归'],
};

export default level;
