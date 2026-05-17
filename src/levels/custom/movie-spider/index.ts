import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "movie-spider",
  title: "电影评分分析",
  category: "实战",
  description: "用 DataFrame 分析电影数据并排序",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '你是电影数据分析师。给6部电影的数据, 计算评分Top-3, 按评分降序打印电影名/评分/票房。...',
  type: "custom",
  difficulty: 4,
  compareMode: "stdout",
  tags: ['pandas', '排序', '过滤'],
};

export default level;
