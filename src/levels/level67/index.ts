import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level67",
  title: "数据预处理实战",
  category: "搭建模型",
  description: "掌握StandardScaler、LabelEncoder等预处理工具",
  content: "",
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 3,
  compareMode: "stdout",
  tags: ['预处理', '标准化', '编码'],
};

export default level;
