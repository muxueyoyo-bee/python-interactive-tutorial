import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen889",
  title: "编写带类型标注的函数: configure",
  category: "中级",
  description: `类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 environment.py（sqlalchemy/alembic）中 \`configure\` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

编写函数 configure(self, connection: Optional[Connection], url: Optional[Union[str, URL]], dialect_name: Optional[str], dialect_opts: Optional[Dict[str, Any]], transactional_ddl: Optional[bool], transaction_per_migration: bool, output_buffer: Optional[TextIO], starting_rev: Optional[str], tag: Optional[str], template_args: Optional[Dict[str, Any]], render_as_batch: bool, target_metadata: Union[MetaData, Sequence[MetaData], None], include_name: Optional[IncludeNameFn], include_object: Optional[IncludeObjectFn], include_schemas: bool, process_revision_directives: Optional[ProcessRevisionDirectiveFn], compare_type: Union[bool, CompareType], compare_server_default: Union[bool, CompareServerDefault], render_item: Optional[RenderItemFn], literal_binds: bool, upgrade_token: str, downgrade_token: str, alembic_module_prefix: str, sqlalchemy_module_prefix: str, user_module_prefix: Optional[str], on_version_apply: Optional[OnVersionApplyFn], autogenerate_plugins: Sequence[str] | None) -> None，返回格式化字符串。

来源：sqlalchemy/alembic — alembic\\runtime\\environment.py`,
  content: "",
  defaultCode: `# 编写带类型标注的函数 configure`,
  answer: "",
  hint: `def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["type-hints", "annotations"],
};

export default level;
