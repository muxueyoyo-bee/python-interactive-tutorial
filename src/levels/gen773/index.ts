import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen773",
  title: "编写带类型标注的函数: update_typeshed",
  category: "中级",
  description: `类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 sync-typeshed.py（python/mypy）中 \`update_typeshed\` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

编写函数 update_typeshed(typeshed_dir: str, commit: str | None) -> str，返回格式化字符串。

来源：python/mypy — misc\\sync-typeshed.py`,
  content: "",
  defaultCode: `# 编写带类型标注的函数 update_typeshed`,
  answer,
  hint: `def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["type-hints", "annotations"],
};

export default level;
