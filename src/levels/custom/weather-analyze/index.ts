import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "weather-analyze",
  title: "天气数据分析",
  category: "实战",
  description: "分析30天温度数据的基本统计",
  content: md,
  defaultCode: 'import numpy as np\n\nnp.random.seed(42)\ntemps = np.random.randint(15, 38, 30)  # 30天温度\n\n# TODO: 计算并打印最高温、最低温、平均温、温差\n# print(f"最高温: {np.max(temps)} C")\n',
  answer,
  hint: '你拿到了某城市30天的每日最高温度数据(列表形式)。计算最高温、最低温、平均温、温差。用 numpy 完成。...',
  type: "custom",
  difficulty: 3,
  compareMode: "stdout",
  tags: ['numpy', '统计'],
};

export default level;
