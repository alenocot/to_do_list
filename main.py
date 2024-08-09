from todo_list import ToDoListManager


def display_menu():
    print("\nTo-Do List Manager")
    print("1. Add a task")
    print("2. List all tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Edit a task")
    print("6. Clear the entire list")
    print("7. Exit")


def main():
    manager = ToDoListManager()

    while True:
        display_menu()
        choice = input("\nEnter your choice: ")

        if choice == '1':
            task = input("Enter the task name: ")
            manager.add_task(task)
            print(f'Task "{task}" added.')

        elif choice == '2':
            tasks = manager.list_tasks()
            if tasks:
                print("\nTasks:")
                for idx, task in enumerate(tasks, 1):
                    status = "Completed" if task["completed"] else "Pending"
                    print(f'{idx}. {task["name"]} [{status}]')
            else:
                print("\nNo tasks found.")

        elif choice == '3':
            task_name = input("Enter the task name to mark as completed: ")
            if manager.mark_task_as_completed(task_name):
                print(f'Task "{task_name}" marked as completed.')
            else:
                print(f'Task "{task_name}" not found.')

        elif choice == '4':
            task_name = input("Enter the task name to delete: ")
            manager.delete_task(task_name)
            print(f'Task "{task_name}" deleted.')

        elif choice == '5':
            old_name = input("Enter the task name to edit: ")
            new_name = input("Enter the new task name: ")
            if manager.edit_task(old_name, new_name):
                print(f'Task "{old_name}" updated to "{new_name}".')
            else:
                print(f'Task "{old_name}" not found.')

        elif choice == '6':
            confirm = input("Are you sure you want to clear the entire list? (yes/no): ")
            if confirm.lower() == 'yes':
                manager.clear_tasks()
                print("All tasks cleared.")

        elif choice == '7':
            print("Exiting the To-Do List Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
