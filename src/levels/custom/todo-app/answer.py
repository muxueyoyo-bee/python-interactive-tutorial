class TodoList:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append({"task": task, "done": False})
        print(f"已添加: {task}")

    def done(self, idx):
        if 0 <= idx < len(self.tasks):
            self.tasks[idx]["done"] = True
            print(f"已完成: {self.tasks[idx]['task']}")

    def show(self):
        for i, t in enumerate(self.tasks):
            mark = "v" if t["done"] else " "
            print(f"[{mark}] {i}. {t['task']}")

todo = TodoList()
todo.add("学习Python")
todo.add("写项目")
todo.add("运动30分钟")
todo.done(0)
todo.show()
