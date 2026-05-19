import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen371",
  title: "编写 try/except 错误处理",
  category: "中级",
  description: `健壮的代码用 try/except 优雅地处理异常。

源文件 check_python_h_first.py 使用了 try/except 捕获多种异常类型。

请仿照此模式编写错误处理代码。

编写 try/except 块：尝试 int('not a number')，捕获 UnicodeDecodeError, ValueError，并在 finally 中打印 'Cleanup complete'。

来源：numpy/numpy — tools\\check_python_h_first.py`,
  content: "",
  defaultCode: `# 编写 try/except/finally 错误处理`,
  answer: "",
  hint: `try: ... except SomeError as e: ... finally: ...`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["error-handling", "try-except"],
};

export default level;
