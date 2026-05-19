import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen178",
  title: "定义异常类层级: CeleryWarning",
  category: "进阶",
  description: `好的代码库用自定义异常类让调用方精确捕获不同错误。

源文件 exceptions.py 定义了如下继承层级：
  • CeleryWarning → UserWarning
  • AlwaysEagerIgnored → CeleryWarning
  • DuplicateNodenameWarning → CeleryWarning
  • FixupWarning → CeleryWarning

请按照这个模式编写这些异常类（每个类只需 pass 语句体）。

定义以下异常类: CeleryWarning(UserWarning), AlwaysEagerIgnored(CeleryWarning), DuplicateNodenameWarning(CeleryWarning), FixupWarning(CeleryWarning)

来源：celery/celery — celery\\exceptions.py`,
  content: "",
  defaultCode: `class CeleryWarning(UserWarning):
    pass

# 定义 AlwaysEagerIgnored, DuplicateNodenameWarning, FixupWarning，继承自 CeleryWarning`,
  answer: "",
  hint: `class 子类名(父类名): —— 父类写在括号里，多个父类用逗号分隔`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["exception", "class", "inheritance"],
};

export default level;
