class Task:
    def __init__(self, title, description, due_date, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.is_completed = False

    def mark_as_completed(self):
        self.is_completed = True

    def __str__(self):
        status = "Completed" if self.is_completed else "Pending"
        return f"{self.title} (Priority: {self.priority}, Due: {self.due_date}) - {status}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        return "\n".join(str(task) for task in self.tasks)

    def mark_task_as_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_as_completed()
                return task
        return None

    def clear_tasks(self):
        self.tasks.clear()


if __name__ == "__main__":
    todo_list = ToDoList()

    # Example interaction (optional for testing)
    task1 = Task("Buy groceries", "Buy milk, eggs, and bread", "2024-08-10", "High")
    task2 = Task("Pay bills", "Pay electricity and water bills", "2024-08-12", "Medium")

    todo_list.add_task(task1)
    todo_list.add_task(task2)

    print(todo_list.list_tasks())

    todo_list.mark_task_as_completed("Buy groceries")
    print("\nAfter marking 'Buy groceries' as completed:\n")
    print(todo_list.list_tasks())

    todo_list.clear_tasks()
    print("\nAfter clearing the tasks:\n")
    print(todo_list.list_tasks())
