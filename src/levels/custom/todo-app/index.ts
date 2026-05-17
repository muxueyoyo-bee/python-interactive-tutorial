import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "todo-app",
  title: "待办事项管理器",
  category: "实战",
  description: "创建任务列表, 支持添加/完成/查看",
  content: md,
  defaultCode: 'class TodoList:\n    def __init__(self):\n        self.tasks = []\n\n    def add(self, task):\n        # 用 {"task": task, "done": False} 格式添加\n        pass\n\n    def done(self, idx):\n        # 把第 idx 个任务的 done 设为 True\n        pass\n\n    def show(self):\n        # 打印所有任务: [v]完成 [ ]未完成 索引. 任务名\n        pass\n\n# 创建实例, 添加"学习Python"/"写项目"/"运动30分钟", 完成第1个, 打印清单',
  answer,
  hint: '实现一个 TodoList 类, 支持 add(task), done(index), show()。添加3个任务, 完...',
  type: "custom",
  difficulty: 3,
  compareMode: "stdout",
  tags: ['列表', '字典', '函数'],
};

export default level;
