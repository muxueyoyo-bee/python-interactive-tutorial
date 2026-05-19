import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen908",
  title: "编写带类型标注的函数: create_proxy_methods",
  category: "中级",
  description: `类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 generate_proxy_methods.py（sqlalchemy/sqlalchemy）中 \`create_proxy_methods\` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

编写函数 create_proxy_methods(target_cls: Type[Any], target_cls_sphinx_name: str, proxy_cls_sphinx_name: str, classmethods: Iterable[str], methods: Iterable[str], attributes: Iterable[str], use_intermediate_variable: Iterable[str]) -> Callable[[Type[_T]], Type[_T]]，返回格式化字符串。

来源：sqlalchemy/sqlalchemy — tools\\generate_proxy_methods.py`,
  content: "",
  defaultCode: `# 编写带类型标注的函数 create_proxy_methods`,
  answer: "",
  hint: `def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["type-hints", "annotations"],
};

export default level;
