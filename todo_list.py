class ToDoListManager:
    def __init__(self):
        self.tasks = []

    # Funcionalidades solicitadas
    def add_task(self, task):
        self.tasks.append({"name": task, "completed": False})

    def list_tasks(self):
        return self.tasks

    def mark_task_as_completed(self, task_name):
        for task in self.tasks:
            if task["name"] == task_name:
                task["completed"] = True
                return True
        return False

    def clear_tasks(self):
        self.tasks.clear()

    # Funcionalidades extras
    def delete_task(self, task_name):
        self.tasks = [task for task in self.tasks if task["name"] != task_name]

    def edit_task(self, old_name, new_name):
        for task in self.tasks:
            if task["name"] == old_name:
                task["name"] = new_name
                return True
        return False
