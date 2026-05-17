import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "password-check",
  title: "密码强度检测器",
  category: "实战",
  description: "判断密码包含的字符种类数",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '写一个 check_password 函数判断密码强度。每满足一项+1分: 长度>=8, 含小写, 含大写, 含数字, ...',
  type: "custom",
  difficulty: 3,
  compareMode: "stdout",
  tags: ['字符串', '正则', '条件'],
};

export default level;
