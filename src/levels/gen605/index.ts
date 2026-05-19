import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen605",
  title: "编写带类型标注的函数: frame_apply",
  category: "中级",
  description: `类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 apply.py（pandas-dev/pandas）中 \`frame_apply\` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

编写函数 frame_apply(obj: DataFrame, func: AggFuncType, axis: Axis, raw: bool, result_type: str | None, by_row: Literal[False, 'compat'], engine: str, engine_kwargs: dict[str, bool] | None, args: Any, kwargs: Any) -> FrameApply，返回格式化字符串。

来源：pandas-dev/pandas — pandas\\core\\apply.py`,
  content: "",
  defaultCode: `# 编写带类型标注的函数 frame_apply`,
  answer,
  hint: `def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["type-hints", "annotations"],
};

export default level;
