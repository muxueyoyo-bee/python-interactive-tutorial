import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "todo-app",
  title: "待办事项管理器",
  category: "实战",
  description: "创建任务列表, 支持添加/完成/查看",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '实现一个 TodoList 类, 支持 add(task), done(index), show()。添加3个任务, 完...',
  type: "custom",
  difficulty: 3,
  compareMode: "stdout",
  tags: ['列表', '字典', '函数'],
};

export default level;
