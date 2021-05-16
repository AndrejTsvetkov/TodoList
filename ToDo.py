
class ToDo:

    def __init__(self, todolist=None):
        if todolist is None:
            self.todolist = []
        else:
            self.todolist = todolist

    def add_task(self, task):
        if task not in self.todolist:
            self.todolist.append(task)

    def delete_task(self, task):
        if task in self.todolist:
            self.todolist.remove(task)

    def print_tasks(self):
        for i in self.todolist:
            print(i)

