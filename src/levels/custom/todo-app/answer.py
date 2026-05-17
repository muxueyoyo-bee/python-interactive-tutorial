class TodoList:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append({"task": task, "done": False})
        print(f"宸叉坊鍔? {task}")

    def done(self, idx):
        if 0 <= idx < len(self.tasks):
            self.tasks[idx]["done"] = True
            print(f"宸插畬鎴? {self.tasks[idx]['task']}")

    def show(self):
        for i, t in enumerate(self.tasks):
            mark = "v" if t["done"] else " "
            print(f"[{mark}] {i}. {t['task']}")

todo = TodoList()
todo.add("瀛︿範Python")
todo.add("鍐欓」鐩?)
todo.add("杩愬姩30鍒嗛挓")
todo.done(0)
todo.show()
