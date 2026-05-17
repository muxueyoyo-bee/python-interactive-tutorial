import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "stock-analyzer",
  title: "股票数据分析",
  category: "实战",
  description: "掌握股票收盘价和均线计算",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '你是一名量化分析师, 拿到了某股票的收盘价数据。用 pandas 计算 5 日和 10 日移动均线, 打印结果(跳过Na...',
  type: "custom",
  difficulty: 3,
  compareMode: "both",
  tags: ['股票', 'pandas', 'matplotlib'],
};

export default level;
