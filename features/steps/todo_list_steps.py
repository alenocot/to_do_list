from behave import given, when, then
from todo_list import ToDoListManager

# Inicializar el ToDoListManager
to_do_manager = ToDoListManager()

# Pasos solicitados
@given('the to-do list is empty')
def step_impl(context):
    to_do_manager.clear_tasks()

@when('the user adds a task "{task}"')
def step_impl(context, task):
    to_do_manager.add_task(task)

@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    tasks = [t['name'] for t in to_do_manager.list_tasks()]
    assert task in tasks, f'Task "{task}" not found in the to-do list'

@given('the to-do list contains tasks:')
def step_impl(context):
    to_do_manager.clear_tasks()
    for row in context.table:
        to_do_manager.add_task(row['Task'])

@when('the user lists all tasks')
def step_impl(context):
    context.tasks = to_do_manager.list_tasks()

@then('the output should contain:')
def step_impl(context):
    task_names = [task['name'] for task in context.tasks]
    for row in context.table:
        assert row['Task'] in task_names, f'Task "{row["Task"]}" not found in output'

@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    to_do_manager.mark_task_as_completed(task)

@then('the to-do list should show task "{task}" as completed')
def step_impl(context, task):
    for t in to_do_manager.list_tasks():
        if t["name"] == task:
            assert t["completed"] is True, f'Task "{task}" is not marked as completed'
            return
    assert False, f'Task "{task}" not found in the to-do list'

@when('the user clears the to-do list')
def step_impl(context):
    to_do_manager.clear_tasks()

@then('the to-do list should be empty')
def step_impl(context):
    assert len(to_do_manager.list_tasks()) == 0, 'The to-do list is not empty'

# Pasos extras
@when('the user deletes the task "{task}"')
def step_impl(context, task):
    to_do_manager.delete_task(task)

@then('the to-do list should contain only "{task}"')
def step_impl(context, task):
    tasks = [t['name'] for t in to_do_manager.list_tasks()]
    assert tasks == [task], f'To-do list contains tasks other than "{task}"'

@when('the user edits the task "{old_task}" to "{new_task}"')
def step_impl(context, old_task, new_task):
    to_do_manager.edit_task(old_task, new_task)