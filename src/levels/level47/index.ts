import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level47",
  title: "线性回归 — 从零实现",
  category: "AI基础",
  description: "用numpy从零实现最小二乘法线性回归，理解拟合原理",
  content: "",
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 3,
  compareMode: "stdout",
  tags: ['线性回归', 'numpy', '梯度下降'],
};

export default level;
