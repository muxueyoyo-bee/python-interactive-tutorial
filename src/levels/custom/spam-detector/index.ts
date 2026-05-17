import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "spam-detector",
  title: "垃圾邮件检测器",
  category: "实战",
  description: "用朴素贝叶斯识别垃圾邮件",
  content: md,
  defaultCode: 'from sklearn.feature_extraction.text import CountVectorizer\nfrom sklearn.naive_bayes import MultinomialNB\nfrom sklearn.model_selection import train_test_split\n\nemails = ["Free money now!!! Click here", "Meeting at 3pm tomorrow",\n          "Claim your prize winner", "Project update attached",\n          "You won lottery cash prize", "Please review the document",\n          "Get rich quick scheme", "Schedule for next week"]\nlabels = [1, 0, 1, 0, 1, 0, 1, 0]  # 1=spam\n\nX_train, X_test, y_train, y_test = train_test_split(emails, labels, test_size=0.25, random_state=42)\n\n# 用 CountVectorizer 把文本转成词频矩阵, 训练 MultinomialNB, 打印准确率',
  answer,
  hint: "用朴素贝叶斯识别垃圾邮件",
  type: "custom",
  difficulty: 4,
  compareMode: "stdout",
  tags: ['NLP', '分类', '朴素贝叶斯'],
};

export default level;
