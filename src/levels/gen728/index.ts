import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen728",
  title: "定义异常类层级: PythonVersionError",
  category: "进阶",
  description: `好的代码库用自定义异常类让调用方精确捕获不同错误。

源文件 exceptions.py 定义了如下继承层级：
  • PythonVersionError → Exception
  • PythonVersionNotFoundError → PythonVersionError
  • NoCompatiblePythonVersionFoundError → PythonVersionError
  • InvalidCurrentPythonVersionError → PythonVersionError

请按照这个模式编写这些异常类（每个类只需 pass 语句体）。

定义以下异常类: PythonVersionError(Exception), PythonVersionNotFoundError(PythonVersionError), NoCompatiblePythonVersionFoundError(PythonVersionError), InvalidCurrentPythonVersionError(PythonVersionError)

来源：python-poetry/poetry — src\\poetry\\utils\\env\\python\\exceptions.py`,
  content: "",
  defaultCode: `class PythonVersionError(Exception):
    pass

# 定义 PythonVersionNotFoundError, NoCompatiblePythonVersionFoundError, InvalidCurrentPythonVersionError，继承自 PythonVersionError`,
  answer,
  hint: `class 子类名(父类名): —— 父类写在括号里，多个父类用逗号分隔`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["exception", "class", "inheritance"],
};

export default level;
