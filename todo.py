import json
import os

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            return json.load(f)
    return[]

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=2)

def add_tasks(tasks):
    task = input("Enter a task: ")
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f"Task '{task}' is added!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
        return
    for index, task in enumerate(tasks):
        status = "✅" if task["done"] else "❌"
        print(f"{index+1}. {status} {task['task']}")

def mark_done(tasks):
    view_tasks(tasks)
    index = int(input("Enter task number to mark as done: ")) -1
    if 0 <= index <= len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("Task marked as done! ✅")
    else:
        print("Invalid task number!")

def delete_task(tasks):
    view_tasks(tasks)
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Task '{removed['task']}' deleted!")
    else:
        print("Invalid task number!")

def main():
    tasks = load_tasks()
    
    while True:
        print("\n📝 To-Do List")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")
        
        choice = input("\nEnter choice (1-5): ")
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Bye! 👋")
            break
        else:
            print("Invalid choice!")

main()