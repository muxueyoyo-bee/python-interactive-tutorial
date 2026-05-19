import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen635",
  title: "编写带类型标注的函数: build_digest_header",
  category: "中级",
  description: `类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 auth.py（psf/requests）中 \`build_digest_header\` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

编写函数 build_digest_header(self, method: str, url: str) -> str | None，返回格式化字符串。

来源：psf/requests — src\\requests\\auth.py`,
  content: "",
  defaultCode: `# 编写带类型标注的函数 build_digest_header`,
  answer,
  hint: `def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["type-hints", "annotations"],
};

export default level;
