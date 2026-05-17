import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "password-check",
  title: "密码强度检测器",
  category: "实战",
  description: "判断密码包含的字符种类数",
  content: md,
  defaultCode: 'import re\n\ndef check_password(pw):\n    # TODO: 每满足一项+1分: 长度>=8, 含小写, 含大写, 含数字, 含特殊符号\n    score = 0\n    # if len(pw) >= 8: score += 1\n    # if re.search(r"[a-z]", pw): score += 1\n    levels = ["弱","一般","中等","强","非常强"]\n    return levels[min(score, 4)]\n\n# TODO: 测试三个密码\n',
  answer,
  hint: '写一个 check_password 函数判断密码强度。每满足一项+1分: 长度>=8, 含小写, 含大写, 含数字, ...',
  type: "custom",
  difficulty: 3,
  compareMode: "stdout",
  tags: ['字符串', '正则', '条件'],
};

export default level;
