import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "color-cluster",
  title: "图片颜色聚类",
  category: "实战",
  description: "用K-Means聚类提取图片主色调",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: "用K-Means聚类提取图片主色调",
  type: "custom",
  difficulty: 4,
  compareMode: "stdout",
  tags: ['聚类', 'KMeans', '图像'],
};

export default level;
