import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen300",
  title: "定义异常类层级: RequestException",
  category: "进阶",
  description: `好的代码库用自定义异常类让调用方精确捕获不同错误。

源文件 exceptions.py 定义了如下继承层级：
  • RequestException → IOError
  • InvalidJSONError → RequestException
  • HTTPError → RequestException
  • ConnectionError → RequestException

请按照这个模式编写这些异常类（每个类只需 pass 语句体）。

定义以下异常类: RequestException(IOError), InvalidJSONError(RequestException), HTTPError(RequestException), ConnectionError(RequestException)

来源：psf/requests — src\\requests\\exceptions.py`,
  content: "",
  defaultCode: `class RequestException(IOError):
    pass

# 定义 InvalidJSONError, HTTPError, ConnectionError，继承自 RequestException`,
  answer: "",
  hint: `class 子类名(父类名): —— 父类写在括号里，多个父类用逗号分隔`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["exception", "class", "inheritance"],
};

export default level;
