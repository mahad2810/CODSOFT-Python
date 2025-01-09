class Task:
    def __init__(self, task, is_complete=False):
        self.task = task
        self.is_complete = is_complete

def show_task_list(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nTask List:")
    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task.is_complete else "Pending"
        print(f"{i}. {task.task} [{status}]")

def add_task(tasks):
    if len(tasks) >= 10:
        print("Task list is full. Cannot add more tasks.")
        return
    task_input = input("Enter task: ").strip()
    tasks.append(Task(task_input))
    print("Task added successfully.")

def edit_task(tasks):
    if not tasks:
        print("No tasks found.")
        return
    show_task_list(tasks)
    try:
        task_number = int(input("Enter the task number to edit: "))
        if task_number < 1 or task_number > len(tasks):
            raise ValueError
        new_task = input("Enter new task: ").strip()
        tasks[task_number - 1].task = new_task
        print("Task edited successfully.")
    except ValueError:
        print("Invalid task number.")

def mark_task_complete(tasks):
    if not tasks:
        print("No tasks found.")
        return
    show_task_list(tasks)
    try:
        task_number = int(input("Enter the task number to mark as complete: "))
        if task_number < 1 or task_number > len(tasks):
            raise ValueError
        tasks[task_number - 1].is_complete = True
        print("Task marked as complete.")
    except ValueError:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Mark Task as Complete")
        print("4. View Tasks")
        print("5. Exit")
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                edit_task(tasks)
            elif choice == 3:
                mark_task_complete(tasks)
            elif choice == 4:
                show_task_list(tasks)
            elif choice == 5:
                print("Exiting the To-Do List. Goodbye...")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
