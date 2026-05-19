import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen138",
  title: "编写带类型标注的函数: url_for",
  category: "中级",
  description: `类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 check_ecosystem.py（astral-sh/ruff）中 \`url_for\` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

编写函数 url_for(self, commit_sha: str, path: str, lnum: int | None) -> str，返回格式化字符串。

来源：astral-sh/ruff — scripts\\check_ecosystem.py`,
  content: "",
  defaultCode: `# 编写带类型标注的函数 url_for`,
  answer: "",
  hint: `def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["type-hints", "annotations"],
};

export default level;
