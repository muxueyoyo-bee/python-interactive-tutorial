import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen686",
  title: "定义异常类层级: ConsoleError",
  category: "进阶",
  description: `好的代码库用自定义异常类让调用方精确捕获不同错误。

源文件 errors.py 定义了如下继承层级：
  • ConsoleError → Exception
  • StyleSyntaxError → ConsoleError
  • StyleStackError → ConsoleError
  • NotRenderableError → ConsoleError

请按照这个模式编写这些异常类（每个类只需 pass 语句体）。

定义以下异常类: ConsoleError(Exception), StyleSyntaxError(ConsoleError), StyleStackError(ConsoleError), NotRenderableError(ConsoleError)

来源：pypa/pip — src\\pip\\_vendor\\rich\\errors.py`,
  content: "",
  defaultCode: `class ConsoleError(Exception):
    pass

# 定义 StyleSyntaxError, StyleStackError, NotRenderableError，继承自 ConsoleError`,
  answer,
  hint: `class 子类名(父类名): —— 父类写在括号里，多个父类用逗号分隔`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["exception", "class", "inheritance"],
};

export default level;
