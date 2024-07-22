class TaskManager:
    def __init__(self):
        self.tasks = []
        print("----WELCOME TO THE TASK MANAGEMENT APP----")

    def add_initial_tasks(self):
        while True:
            try:
                total_task = int(input("Enter how many tasks you want to add: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        for i in range(1, total_task + 1):
            task_name = input(f"Enter task {i}: ")
            self.tasks.append(task_name)

        print(f"Today's tasks are:\n{self.tasks}")

    def add_task(self):
        add = input("Enter task you want to add: ")
        self.tasks.append(add)
        print(f"Task '{add}' has been successfully added...")

    def update_task(self):
        update_val = input("Enter the task name you want to update: ")
        if update_val in self.tasks:
            up = input("Enter new task: ")
            ind = self.tasks.index(update_val)
            self.tasks[ind] = up
            print(f"Task '{update_val}' has been successfully updated to '{up}'")
        else:
            print(f"Task '{update_val}' not found in the list.")

    def delete_task(self):
        delete_val = input("Which task do you want to delete: ")
        if delete_val in self.tasks:
            self.tasks.remove(delete_val)
            print(f"Task '{delete_val}' has been successfully deleted...")
        else:
            print(f"Task '{delete_val}' not found in the list.")

    def view_tasks(self):
        print(f"Total tasks: {self.tasks}")

    def run(self):
        self.add_initial_tasks()
        while True:
            try:
                operation = int(input("Enter 1 to Add\n2 to Update\n3 to Delete\n4 to View\n5 to Exit: "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")
                continue

            if operation == 1:
                self.add_task()
            elif operation == 2:
                self.update_task()
            elif operation == 3:
                self.delete_task()
            elif operation == 4:
                self.view_tasks()
            elif operation == 5:
                print("Closing the program....")
                break
            else:
                print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.run()
