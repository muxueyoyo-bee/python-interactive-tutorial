import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen704",
  title: "编写带类型标注的函数: send",
  category: "中级",
  description: `类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 adapter.py（pypa/pip）中 \`send\` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

编写函数 send(self, request: PreparedRequest, stream: bool, timeout: None | float | tuple[float, float] | tuple[float, None], verify: bool | str, cert: None | bytes | str | tuple[bytes | str, bytes | str], proxies: Mapping[str, str] | None, cacheable_methods: Collection[str] | None) -> Response，返回格式化字符串。

来源：pypa/pip — src\\pip\\_vendor\\cachecontrol\\adapter.py`,
  content: "",
  defaultCode: `# 编写带类型标注的函数 send`,
  answer,
  hint: `def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["type-hints", "annotations"],
};

export default level;
