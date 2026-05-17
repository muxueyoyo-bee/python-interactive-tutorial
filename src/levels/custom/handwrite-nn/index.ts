import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "handwrite-nn",
  title: "手写数字识别",
  category: "实战",
  description: "用MLP神经网络识别手写数字(0-9)",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: "用MLP神经网络识别手写数字(0-9)",
  type: "custom",
  difficulty: 5,
  compareMode: "stdout",
  tags: ['神经网络', 'numpy', 'MNIST'],
};

export default level;
