print("Welcome to your Personal To-Do list!")

while True:
    action = input(
        "What would you like to do? (add, view, mark task complete, delete task, exit): ").lower()

    if action == "add":
        task = input("Enter the Task you would like to add: ")
        due_date = input("Enter the Due Date of the Task(MM-DD-YYYY): ")
        with open("todo_list.txt", "a") as file:
            file.write(f"{task} | {due_date} | TODO\n")
        print(f"Task '{task}' added successfully!")

    elif action == "view":
        with open("todo_list.txt", "r") as file:
            tasks = file.readlines()
        if not tasks:
            print("You have no tasks to view.")
            continue
        if tasks:
            print("Your To-Do list:")
            print("Task Number | Task | Due Date | Status")
            print("-" * 38)
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
        
       

    elif action == "mark task complete":
        with open("todo_list.txt", "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("Your To-Do list is empty.")
            continue

        print("Your To-Do list:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")

        task_number = int(
            input("Enter the number of the task you would like to mark as complete: "))

        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1] = "[DONE] " + tasks[task_number - 1]
            with open("todo_list.txt", "w") as file:
                file.writelines(tasks)
            print("Task marked as complete successfully!")
        else:
            print("Incorrect Task Number. Try again.")

    elif action == "delete task":
        with open("todo_list.txt", "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("Your To-Do list is empty.")
            continue

        print("Your To-Do list:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")

        task_number = int(
            input("Enter the number of the task you would like to delete: ")
        )

        if 1 <= task_number <= len(tasks):
            del tasks[task_number - 1]
            with open("todo_list.txt", "w") as file:
                file.writelines(tasks)
            print("Task deleted successfully!")
        else:
            print("Invalid Task Number. Please try again.")

    elif action == "exit":
        print("See you Later for more Tasks!")
        break

    else:
        print("Try again!")
