import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen783",
  title: "编写带类型标注的函数: build",
  category: "中级",
  description: `类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 build.py（python/mypy）中 \`build\` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

编写函数 build(sources: list[BuildSource], options: Options, alt_lib_path: str | None, flush_errors: Callable[[str | None, list[str], bool], None] | None, fscache: FileSystemCache | None, stdout: TextIO | None, stderr: TextIO | None, extra_plugins: Sequence[Plugin] | None, worker_env: Mapping[str, str] | None) -> BuildResult，返回格式化字符串。

来源：python/mypy — mypy\\build.py`,
  content: "",
  defaultCode: `# 编写带类型标注的函数 build`,
  answer,
  hint: `def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["type-hints", "annotations"],
};

export default level;
