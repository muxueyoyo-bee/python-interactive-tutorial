import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen374",
  title: "编写带类型标注的函数: get_request_handler",
  category: "中级",
  description: `类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 routing.py（fastapi/fastapi）中 \`get_request_handler\` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

编写函数 get_request_handler(dependant: Dependant, body_field: ModelField | None, status_code: int | None, response_class: type[Response] | DefaultPlaceholder, response_field: ModelField | None, response_model_include: IncEx | None, response_model_exclude: IncEx | None, response_model_by_alias: bool, response_model_exclude_unset: bool, response_model_exclude_defaults: bool, response_model_exclude_none: bool, dependency_overrides_provider: Any | None, embed_body_fields: bool, strict_content_type: bool | DefaultPlaceholder, stream_item_field: ModelField | None, is_json_stream: bool) -> Callable[[Request], Coroutine[Any, Any, Response]]，返回格式化字符串。

来源：fastapi/fastapi — fastapi\\routing.py`,
  content: "",
  defaultCode: `# 编写带类型标注的函数 get_request_handler`,
  answer: "",
  hint: `def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["type-hints", "annotations"],
};

export default level;
