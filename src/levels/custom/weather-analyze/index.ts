import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "weather-analyze",
  title: "天气数据分析",
  category: "实战",
  description: "分析30天温度数据的基本统计",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '你拿到了某城市30天的每日最高温度数据(列表形式)。计算最高温、最低温、平均温、温差。用 numpy 完成。...',
  type: "custom",
  difficulty: 3,
  compareMode: "stdout",
  tags: ['numpy', '统计'],
};

export default level;
