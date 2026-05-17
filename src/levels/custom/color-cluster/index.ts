import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "color-cluster",
  title: "图片颜色聚类",
  category: "实战",
  description: "用K-Means聚类提取图片主色调",
  content: md,
  defaultCode: 'import numpy as np\nfrom sklearn.cluster import KMeans\n\nnp.random.seed(42)\npixels = np.random.randint(0, 256, (200, 3))  # 模拟图片像素\n\n# TODO: 用 KMeans 聚成 5 类 (n_clusters=5, random_state=42, n_init=10)\n# kmeans = KMeans(...)\n# kmeans.fit(pixels)\n\n# TODO: 获取聚类中心, 打印5种主色调的RGB值和像素占比\n# colors = kmeans.cluster_centers_.astype(int)\n# labels = kmeans.labels_\n',
  answer,
  hint: "用K-Means聚类提取图片主色调",
  type: "custom",
  difficulty: 4,
  compareMode: "stdout",
  tags: ['聚类', 'KMeans', '图像'],
};

export default level;
