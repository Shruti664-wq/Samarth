class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f'Added task: "{task}"')

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
            return

        for i, task in enumerate(self.tasks, 1):
            status = "Done" if task["completed"] else "Pending"
            print(f"{i}. {task['task']} - {status}")

    def complete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f'Task "{self.tasks[task_number - 1]["task"]}" marked as completed.')
        else:
            print("Invalid task number.")

    def remove_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f'Removed task: "{removed_task["task"]}"')
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_number = int(input("Enter the task number to mark as completed: "))
            todo_list.complete_task(task_number)
        elif choice == "4":
            task_number = int(input("Enter the task number to remove: "))
            todo_list.remove_task(task_number)
        elif choice == "5":
            print("Exiting the to-do list program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()