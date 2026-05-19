import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen741",
  title: "编写上下文管理器: LazyFileOverHTTP",
  category: "进阶",
  description: `上下文管理器（Context Manager）用 with 语句管理资源的获取和释放。

源文件 lazy_wheel.py 定义了类 \`LazyFileOverHTTP\`，实现了 __enter__ / __exit__。

请仿照此模式编写一个上下文管理器，在进入和退出时打印信息。

编写类 LazyFileOverHTTP，实现 __enter__ 和 __exit__，进入时打印 'Entering {name}'，退出时打印 'Exiting {name}'。

来源：python-poetry/poetry — src\\poetry\\inspection\\lazy_wheel.py`,
  content: "",
  defaultCode: `# 编写上下文管理器 LazyFileOverHTTP`,
  answer,
  hint: `实现 __enter__(self) 返回 self，__exit__(self, exc_type, exc_val, exc_tb) 处理清理`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["context-manager", "class", "with-statement"],
};

export default level;
