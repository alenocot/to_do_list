from behave import given, when, then
from todo_list import ToDoList, Task

@given('the to-do list is empty')
def step_given_todo_list_empty(context):
    context.todo_list = ToDoList()

@when('the user adds a task "{title}" with description "{description}" due on "{due_date}" and priority "{priority}"')
def step_when_add_task(context, title, description, due_date, priority):
    task = Task(title, description, due_date, priority)
    context.todo_list.add_task(task)

@then('the to-do list should contain "{title}"')
def step_then_todo_list_should_contain(context, title):
    tasks = [task.title for task in context.todo_list.tasks]
    assert title in tasks

@given('the to-do list contains tasks:')
def step_given_todo_list_contains_tasks(context):
    context.todo_list = ToDoList()
    for row in context.table:
        task = Task(row['Task'], "", "", "")
        context.todo_list.add_task(task)

@when('the user lists all tasks')
def step_when_user_lists_tasks(context):
    context.task_list_output = context.todo_list.list_tasks()

@then('the output should contain:')
def step_then_output_should_contain(context):
    for row in context.text.strip().splitlines():
        assert row in context.task_list_output

@when('the user marks task "{title}" as completed')
def step_when_user_marks_task_completed(context, title):
    context.todo_list.mark_task_as_completed(title)

@then('the to-do list should show task "{title}" as completed')
def step_then_todo_list_should_show_completed(context, title):
    task = next((task for task in context.todo_list.tasks if task.title == title), None)
    assert task is not None and task.is_completed

@when('the user clears the to-do list')
def step_when_user_clears_todo_list(context):
    context.todo_list.clear_tasks()

@then('the to-do list should be empty')
def step_then_todo_list_should_be_empty(context):
    assert len(context.todo_list.tasks) == 0

@when('the user adds a task "{title}" with description "{description}" due on "{due_date}" and priority "{priority}"')
def step_when_add_task(context, title, description, due_date, priority):
    task = Task(title, description, due_date, priority)
    context.todo_list.add_task(task)

@then('the to-do list should contain "{count}" tasks with the title "{title}"')
def step_then_todo_list_should_contain_multiple(context, count, title):
    tasks = [task for task in context.todo_list.tasks if task.title == title]
    assert len(tasks) == int(count)

@when('the user lists only completed tasks')
def step_when_user_lists_completed_tasks(context):
    context.task_list_output = "\n".join(str(task) for task in context.todo_list.tasks if task.is_completed)

@then('the output should not contain:')
def step_then_output_should_not_contain(context):
    for row in context.text.strip().splitlines():
        assert row not in context.task_list_output
