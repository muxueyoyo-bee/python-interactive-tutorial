import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "color-cluster",
  title: "图片颜色聚类",
  category: "实战",
  description: "用K-Means聚类提取图片主色调",
  content: md,
  defaultCode: 'import numpy as np\nfrom sklearn.cluster import KMeans\n\nnp.random.seed(42)\npixels = np.random.randint(0, 256, (200, 3))  # 200个像素的RGB值\n\n# 用 KMeans(n_clusters=5) 聚类, 打印5种主色调的RGB值和像素占比',
  answer,
  hint: "用K-Means聚类提取图片主色调",
  type: "custom",
  difficulty: 4,
  compareMode: "stdout",
  tags: ['聚类', 'KMeans', '图像'],
};

export default level;
