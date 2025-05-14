import os
import json

#Global Constants
FILENAME = "Day4_Tasks.json"

# This will store all task in memory
# Format: {"Work": [{"task":"Send email", "done": False}], ...}
tasks = {}

# Load tasks from file
def load_tasks():
    global tasks
    if os.path.exists(FILENAME):
        with open(FILENAME,"r") as file:
            try:
                tasks =json.load(file)
            except json.JSONDecodeError:
                print("Corrupted File. Starting Fresh")
                tasks = {}
            
# Save tasks to file
def save_tasks():
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent = 4)
    
def show_menu():
    print("\n=== Task Manager ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Save Tasks")
    print("6. Exit")

# Add a new task
def add_task():
    category = input("Enter task category (e.g., Work, Home, Fitness): ").strip()
    task_desc = input("Enter task description: ").strip()

    if category not in tasks:
        tasks[category] = []

    tasks[category].append({
        "task": task_desc,
        "done": False
    })
    print("Task Added.")

# View all tasks 
def view_tasks():
    if not tasks:
        print("No tasks found.")
        return
    
    print("\n--- All tasks ---")
    for category, task_list in tasks.items():
        print(f"\nCategory: {category}")
        for i, task in enumerate(task_list):
            status = "✔️" if task["done"] else "❌"
            print(f"{i+1}.[{status}] {task['task']}")

# Mark a test as done
def mark_task_done():
    category = input("Enter a category: ").strip()
    if category not in tasks or not tasks[category]:
        print("No such category or empty.")
        return

    view_tasks_in_category(category)

    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks[category]):
            tasks[category][index]["done"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number")
    except ValueError:
        print("Enter a valid number")

# View tasks in a specific category
def view_tasks_in_category(category):
    print(f"\nTasks in {category}:")
    for i,task in enumerate(tasks[category]):
        status = "✔️" if task["done"] else "❌"
        print(f"{i+1}.[{status}] {task['task']}")

# Delete a task
def delete_task():
    category = input("Enter category: ").strip()
    if category not in tasks or not tasks[category]:
        print("No such category or empty")
        return
    
    view_tasks_in_category(category)

    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks[category]):
            deleted = tasks[category].pop(index)
            print(f"Deleted : {deleted['task']}")
            if not tasks[category]:
                del tasks[category]
            else:
                print("Invalid task number")

    except ValueError:
        print("Please enter a valid number.")

# Main program
def main():
    load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option(1-6): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            save_tasks()
            print("Tasks saved.")
        elif choice == "6":
            save_tasks()
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

# Entry point
if __name__ == "__main__":
    main()