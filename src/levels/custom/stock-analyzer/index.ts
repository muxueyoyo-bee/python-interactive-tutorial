import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "stock-analyzer",
  title: "股票数据分析",
  category: "实战",
  description: "掌握股票收盘价和均线计算",
  content: md,
  defaultCode: 'import pandas as pd\nimport numpy as np\n\nnp.random.seed(42)\ndates = pd.date_range("2025-01-01", periods=20)\ndf = pd.DataFrame({"close": np.cumsum(np.random.randn(20)) + 100})\n\n# TODO: 计算 5日 和 10日 移动均线\n# df["ma5"] = df["close"].rolling(window=...).mean()\n# df["ma10"] = df["close"].rolling(window=...).mean()\n\n# TODO: print(df[["close","ma5","ma10"]].dropna().round(2))\n',
  answer,
  hint: '你是一名量化分析师, 拿到了某股票的收盘价数据。用 pandas 计算 5 日和 10 日移动均线, 打印结果(跳过Na...',
  type: "custom",
  difficulty: 3,
  compareMode: "both",
  tags: ['股票', 'pandas', 'matplotlib'],
};

export default level;
