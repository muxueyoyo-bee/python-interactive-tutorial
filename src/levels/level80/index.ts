import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level80",
  title: "偏差与方差的权衡",
  category: "AI进阶",
  description: "掌握偏差与方差的权衡的核心概念与实现",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 4,
  compareMode: "stdout",
  tags: ['偏差-方差', '过拟合', '欠拟合'],
};

export default level;
