def task():
    tasks = []
    print("----WELCOME TO THE TASK MANAGEMENT APP----")

    while True:
        try:
            total_task = int(input("Enter how many tasks you want to add: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)

    print(f"Today's tasks are:\n{tasks}")

    while True:
        try:
            operation = int(input("Enter 1 to Add\n2 to Update\n3 to Delete\n4 to View\n5 to Exit: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if operation == 1:
            add = input("Enter task you want to add: ")
            tasks.append(add)
            print(f"Task '{add}' has been successfully added...")

        elif operation == 2:
            update_val = input("Enter the task name you want to update: ")
            if update_val in tasks:
                up = input("Enter new task: ")
                ind = tasks.index(update_val)
                tasks[ind] = up
                print(f"Task '{update_val}' has been successfully updated to '{up}'")
            else:
                print(f"Task '{update_val}' not found in the list.")

        elif operation == 3:
            delete_val = input("Which task do you want to delete: ")
            if delete_val in tasks:
                tasks.remove(delete_val)
                print(f"Task '{delete_val}' has been successfully deleted...")
            else:
                print(f"Task '{delete_val}' not found in the list.")

        elif operation == 4:
            print(f"Total tasks: {tasks}")

        elif operation == 5:
            print("Closing the program....")
            break

        else:
            print("Invalid input. Please enter a number between 1 and 5.")

task()
