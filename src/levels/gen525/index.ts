import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen525",
  title: "定义异常类层级: ResolverException",
  category: "进阶",
  description: `好的代码库用自定义异常类让调用方精确捕获不同错误。

源文件 exceptions.py 定义了如下继承层级：
  • ResolverException → Exception
  • RequirementsConflicted → ResolverException, Generic[RT, CT]
  • InconsistentCandidate → ResolverException, Generic[RT, CT]
  • ResolutionError → ResolverException

请按照这个模式编写这些异常类（每个类只需 pass 语句体）。

定义以下异常类: ResolverException(Exception), RequirementsConflicted(ResolverException, Generic[RT, CT]), InconsistentCandidate(ResolverException, Generic[RT, CT]), ResolutionError(ResolverException)

来源：pypa/pip — src\\pip\\_vendor\\resolvelib\\resolvers\\exceptions.py`,
  content: "",
  defaultCode: `class ResolverException(Exception):
    pass

# 定义 RequirementsConflicted, InconsistentCandidate, ResolutionError，继承自 ResolverException`,
  answer: "",
  hint: `class 子类名(父类名): —— 父类写在括号里，多个父类用逗号分隔`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["exception", "class", "inheritance"],
};

export default level;
