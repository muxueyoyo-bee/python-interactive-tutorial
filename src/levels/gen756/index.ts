import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen756",
  title: "编写带类型标注的函数: get_package_from_vcs",
  category: "中级",
  description: `类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 direct_origin.py（python-poetry/poetry）中 \`get_package_from_vcs\` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

编写函数 get_package_from_vcs(vcs: str, url: str, branch: str | None, tag: str | None, rev: str | None, subdirectory: str | None, source_root: Path | None) -> Package，返回格式化字符串。

来源：python-poetry/poetry — src\\poetry\\packages\\direct_origin.py`,
  content: "",
  defaultCode: `# 编写带类型标注的函数 get_package_from_vcs`,
  answer,
  hint: `def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["type-hints", "annotations"],
};

export default level;
