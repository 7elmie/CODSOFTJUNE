class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def mark_task_as_completed(self, task):
        task.completed = True

    def display_tasks(self):
        print("Tasks:")
        for idx, task in enumerate(self.tasks, start=1):
            status = "✓" if task.completed else " "
            print(f"{idx}. [{status}] {task.description}")

def main():
    to_do_list = ToDoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Remove Task")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            task = Task(description)
            to_do_list.add_task(task)
        elif choice == '2':
            to_do_list.display_tasks()
            task_index = int(input("Enter the task number to mark as completed: ")) - 1
            task = to_do_list.tasks[task_index]
            to_do_list.mark_task_as_completed(task)
            print("Task marked as completed.")
        elif choice == '3':
            to_do_list.display_tasks()
            task_index = int(input("Enter the task number to remove: ")) - 1
            task = to_do_list.tasks[task_index]
            to_do_list.remove_task(task)
            print("Task removed.")
        elif choice == '4':
            to_do_list.display_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
