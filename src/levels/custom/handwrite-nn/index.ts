import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "handwrite-nn",
  title: "手写数字识别",
  category: "实战",
  description: "用MLP神经网络识别手写数字(0-9)",
  content: md,
  defaultCode: 'import numpy as np\nfrom sklearn.datasets import load_digits\nfrom sklearn.neural_network import MLPClassifier\nfrom sklearn.model_selection import train_test_split\n\ndigits = load_digits()\nX_train, X_test, y_train, y_test = train_test_split(\n    digits.data, digits.target, test_size=0.2, random_state=42)\nX_train = X_train / 16.0   # 像素值归一化\nX_test = X_test / 16.0\n\n# 创建 MLPClassifier(hidden_layer_sizes=(64,32), max_iter=500) 并训练\n# 打印测试准确率和隐藏层结构',
  answer,
  hint: "用MLP神经网络识别手写数字(0-9)",
  type: "custom",
  difficulty: 5,
  compareMode: "stdout",
  tags: ['神经网络', 'numpy', 'MNIST'],
};

export default level;
