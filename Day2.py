#To-do List Manger

import os

# File to save tasks
FILENAME = "todo.txt"
task_id_counter = 1

# List to hold tasks
tasks =[]

# Load Tasks from file if available
def load_tasks():
    global task_id_counter
    if not os.path.exists(FILENAME):
        return
    with open(FILENAME, "r") as file:
        for line in file:
            parts = line.strip().split("::")
            if len(parts) == 3:
                id_, title, is_done = parts
                tasks.append({
                    "id": int(id_),
                    "title": title,
                    "is_done": is_done == "True"
                })
                task_id_counter = max(task_id_counter, int(id_) + 1)
            
# Save current tasks to file
def save_tasks():
    with open(FILENAME,"w") as file:
        for task in tasks:
            file.write(f"{task['id']}::{task['title']}::{task['is_done']}\n")
        
# Display Menu options
def display_menu():
    print("\n==== To-do List Manager ====")
    print("1. View Tasks.")
    print("2. Add Tasks.")
    print("3. Mark Task as completed.")
    print("4. Delete Task.")
    print("5. Save and exit.")

def view_tasks():
    if not tasks:
        print("No tasks found.")
        return
    print("\n--- Pending Tasks ---")
    for task in tasks:
        if not task["is_done"]:
            print(f"[{task['id']}] {task['title']}")
    print("\n--- Completed Tasks ---")
    for task in tasks:
        if task["is_done"]:
            print(f"[{task['id']}] {task['title']} (done)")
        
# Add a new task
def add_task():
    global task_id_counter
    title = input("Enter Task title: ").strip()
    if not title:
        print("Task cannot be empty.")
        return
    task = {
        "id": task_id_counter,
        "title": title,
        "is_done": False
    }
    tasks.append(task)
    task_id_counter += 1
    print(f"Task added with ID {task['id']}.")

# Mark a task as completed.
def complete_task():
    try:
        id_ = int(input("Enter task ID to mark as done: "))
    except ValueError:
        print("Invalid Input")
        return
    for task in tasks:
        if task["id"] == id_:
            if task["is_done"]:
                print("Task is already marked as done.")
            else:
                task["is_done"] = True
                print("Task marked as done.")
            return
        print("Task ID not found.")

# Delete a task by ID
def delete_task():
    try:
        id_ = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Invalid Input")
    for i, task in enumerate(tasks):
        if task["id"] == id_:
            del tasks[i]
            print("Task Deleted.")
            return
    print("Task id not found")

# Run the Application
def main():
    load_tasks()
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            save_tasks()
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid Choice. Please try again.")
        
# Entry Point
if __name__ == "__main__":
    main()