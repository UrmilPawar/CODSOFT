tasks = []

class Task:
    def __init__(self, title, description="", status="Pending"):
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"Title: {self.title}, Description: {self.description}, Status: {self.status}"

def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description (optional): ")
    tasks.append(Task(title, description))
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def update_task():
    view_tasks()
    if not tasks:
        return
    try:
        task_index = int(input("Enter the task number to update: ")) - 1
        if 0 <= task_index < len(tasks):
            print("1. Update Title")
            print("2. Update Description")
            print("3. Update Status")
            choice = input("Select an option: ")
            if choice == "1":
                tasks[task_index].title = input("Enter new title: ")
            elif choice == "2":
                tasks[task_index].description = input("Enter new description: ")
            elif choice == "3":
                tasks[task_index].status = input("Enter new status (e.g., Pending/Completed): ")
            else:
                print("Invalid option.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks.pop(task_index)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    while True:
        display_menu()
        choice = input("Select an option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
