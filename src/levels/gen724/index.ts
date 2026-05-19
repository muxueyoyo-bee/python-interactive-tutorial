import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen724",
  title: "定义异常类层级: PoetryConsoleError",
  category: "进阶",
  description: `好的代码库用自定义异常类让调用方精确捕获不同错误。

源文件 exceptions.py 定义了如下继承层级：
  • PoetryConsoleError → CleoError
  • GroupNotFoundError → PoetryConsoleError
  • PoetryRuntimeError → PoetryConsoleError

请按照这个模式编写这些异常类（每个类只需 pass 语句体）。

定义以下异常类: PoetryConsoleError(CleoError), GroupNotFoundError(PoetryConsoleError), PoetryRuntimeError(PoetryConsoleError)

来源：python-poetry/poetry — src\\poetry\\console\\exceptions.py`,
  content: "",
  defaultCode: `class PoetryConsoleError(CleoError):
    pass

# 定义 GroupNotFoundError, PoetryRuntimeError，继承自 PoetryConsoleError`,
  answer,
  hint: `class 子类名(父类名): —— 父类写在括号里，多个父类用逗号分隔`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["exception", "class", "inheritance"],
};

export default level;
