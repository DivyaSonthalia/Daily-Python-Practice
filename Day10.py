import time

class Task:
    def __init__(self, name):
        self.name = name
        self.total_time = 0 #in seconds
        self.start_time = None #when the timer started
        self.running = False

    def start(self):
        if self.running:
            print(f"Task'{self.name}' is already running.")
            return
        self.start_time = time.time()
        self.running = True
        print(f"Started Task {self.name}")

    def stop(self):
        if not self.running:
            print(f"Task '{self.name}' is not running")
            return
        elapsed = time.time() - self.start_time
        self.total_time += elapsed
        self.running = False
        self.start_time = None
        print(f"Stopped Task '{self.name}'. Time added:{int(elapsed)} sec")

    def status(self):
        current = self.total_time
        if self.running:
            current += time.time() - self.start_time
        return int(current)
    
    def __str__(self):
        status = "Running" if self.running else "Stopped"
        return f"{self.name} - {status} | Total Time: {self.status()} sec"
    
class TaskTracker:
    def __init__(self):
        self.tasks = {}

    def add_task(self):
        name = input("Enter task name: ").strip()
        if name in self.tasks:
            print("Tasks already exists")
            return
        self.tasks[name] = Task(name)
        print(f"Task '{name}' added")

    def start_task(self):
        name = input("Enter task name to start: ").strip()
        task = self.tasks.get(name)
        if task:
            task.start()
        else:
            print("Task not found.")
        
    def stop_task(self):
        name = input("Enter task name to stop: ").strip()
        task = self.tasks.get(name)
        if task:
            task.stop()
        else:
            print("Task not found")
        
    def view_tasks(self):
        if not self.tasks:
            print("📭 No tasks yet.")
            return
        print("\n🗂️ All Tasks:")
        for task in self.tasks.values():
            print(task)
        
    def delete_task(self):
        name = input("Enter task name to delete: ").strip()
        if name in self.tasks:
            del self.tasks[name]
            print(f"Task name '{name}' deleted")
        else:
            print("Task not found")

    def show_menu(self):
        print("Task timer menu")
        print("1. Add task")
        print("2. Start task")
        print("3. Stop task")
        print("4. View all tasks")
        print("5. Delete task")
        print("6. Exit")

    def run(self):
        print("Welcome to timer app.")
        while True:
            self.show_menu()
            choice = input("Select an option(1-6): ").strip()
            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.start_task()
            elif choice == '3':
                self.stop_task()
            elif choice == '4':
                self.view_tasks()
            elif choice == '5':
                self.delete_task()
            elif choice == '6':
                print("👋 Exiting Task Timer. Stay productive!")
                break
            else:
                print("❌ Invalid choice! Try again.")

if __name__ == "__main__":
    tracker = TaskTracker()
    tracker.run()
