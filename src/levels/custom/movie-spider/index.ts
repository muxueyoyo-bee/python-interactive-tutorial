import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "movie-spider",
  title: "电影评分分析",
  category: "实战",
  description: "用 DataFrame 分析电影数据并排序",
  content: md,
  defaultCode: 'import pandas as pd\n\ndata = {\n    "电影": ["流浪地球", "满江红", "封神", "无名", "深海", "长安三万里"],\n    "评分": [7.9, 6.7, 7.3, 6.5, 7.6, 8.3],\n    "票房": [46.8, 45.4, 26.3, 9.3, 9.2, 18.2],\n}\ndf = pd.DataFrame(data)\n\n# TODO: 按评分降序, 取Top-3, 打印电影名/评分/票房\n# top = df.sort_values("评分", ascending=False).head(3)\n# print(top[["电影","评分","票房"]].to_string(index=False))\n',
  answer,
  hint: '你是电影数据分析师。给6部电影的数据, 计算评分Top-3, 按评分降序打印电影名/评分/票房。...',
  type: "custom",
  difficulty: 4,
  compareMode: "stdout",
  tags: ['pandas', '排序', '过滤'],
};

export default level;
