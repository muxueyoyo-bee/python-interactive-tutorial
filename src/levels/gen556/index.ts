import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen556",
  title: "编写 try/except 错误处理",
  category: "中级",
  description: `健壮的代码用 try/except 优雅地处理异常。

源文件 environment.py 使用了 try/except 捕获多种异常类型。

请仿照此模式编写错误处理代码。

编写 try/except 块：尝试 int('not a number')，捕获 (AttributeError, TypeError, LookupError), (TemplateNotFound, UndefinedError), (TypeError, LookupError, AttributeError)，并在 finally 中打印 'Cleanup complete'。

来源：pallets/jinja — src\\jinja2\\environment.py`,
  content: "",
  defaultCode: `# 编写 try/except/finally 错误处理`,
  answer,
  hint: `try: ... except SomeError as e: ... finally: ...`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["error-handling", "try-except"],
};

export default level;
