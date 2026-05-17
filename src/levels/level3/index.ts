import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level3",
  title: "数据类型 — Python 里的各种'东西'",
  category: "基础语法",
  description: "认识 Python 的基本数据类型",
  content: md,
  defaultCode: "# 请在此处编写代码\nint_var = 42\nfloat_var = 3.14\nstr_var = \"Python\"\nbool_var = True\n\nprint()",
  answer,
  hint: "使用 type() 函数查看变量的类型，例如 type(int_var)",
  type: "main",
  difficulty: 1,
  compareMode: "stdout",
  tags: ["数据类型", "int", "float", "str", "bool"],
};

export default level;
