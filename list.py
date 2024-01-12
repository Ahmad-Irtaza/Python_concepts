todo_list = []

def add_task(task):
    """Add a task to the to-do list."""
    todo_list.append({'Task': task, 'Completed': False})
    print(f"Task '{task}' added to the to-do list.")

def complete_task(index):
    """Mark a task as completed."""
    if 0 <= index < len(todo_list):
        todo_list[index]['Completed'] = True
        print(f"Task '{todo_list[index]['Task']}' marked as completed.")
    else:
        print("Invalid task index.")

def display_todo_list():
    """Display the current to-do list."""
    if not todo_list:
        print("The to-do list is empty.")
    else:
        print("To-Do List:")
        for i, task_info in enumerate(todo_list):
            status = "Completed" if task_info['Completed'] else "Not Completed"
            print(f"{i + 1}. {task_info['Task']} - {status}")

# Example usage
add_task("ready for uni")
add_task("prepare for quiz")
add_task("then enjoy")

complete_task(1)

display_todo_list()
