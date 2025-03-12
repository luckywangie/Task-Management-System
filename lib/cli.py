import sqlite3
import os

DB_PATH = "lib/db/database.db"

def connect_db():
    return sqlite3.connect(DB_PATH)

def create_task(title, description, due_date):
    """Add a new task to the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, description, due_date, completed) VALUES (?, ?, ?, ?)", 
                   (title, description, due_date, False))
    conn.commit()
    conn.close()
    print("\n✅ Task added successfully!")

def list_tasks():
    """List all tasks from the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, due_date, completed FROM tasks")
    tasks = cursor.fetchall()
    conn.close()

    print("\n📋 Your Tasks:")
    if not tasks:
        print("   No tasks available.")
    else:
        for task in tasks:
            status = "✅" if task[3] else "❌"
            print(f"   {status} [{task[0]}] {task[1]} (Due: {task[2]})")
    print("\n")

def view_task(task_id):
    """View details of a specific task."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    task = cursor.fetchone()
    conn.close()

    if task:
        status = "✅ Completed" if task[4] else "❌ Pending"
        print(f"\n📌 Task Details:\n   Title: {task[1]}\n   Description: {task[2]}\n   Due Date: {task[3]}\n   Status: {status}\n")
    else:
        print("\n❌ Task not found.")

def update_task(task_id, status):
    """Update task completion status."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed = ? WHERE id = ?", (status, task_id))
    conn.commit()
    conn.close()
    print("\n✏️ Task updated successfully!")

def delete_task(task_id):
    """Delete a task from the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    print("\n🗑 Task deleted successfully!")

def filter_tasks(status):
    """Filter tasks by completion status."""
    conn = connect_db()
    cursor = conn.cursor()
    completed_status = True if status == "completed" else False
    cursor.execute("SELECT id, title, due_date FROM tasks WHERE completed = ?", (completed_status,))
    tasks = cursor.fetchall()
    conn.close()

    print(f"\n📋 {status.capitalize()} Tasks:")
    if not tasks:
        print("   No tasks found.")
    else:
        for task in tasks:
            print(f"   [{task[0]}] {task[1]} (Due: {task[2]})")
    print("\n")

def show_menu():
    """Display the menu."""
    print("\n📌 Task Management System")
    print("1️⃣  List Tasks")
    print("2️⃣  Add Task")
    print("3️⃣  View Task Details")
    print("4️⃣  Update Task Status")
    print("5️⃣  Delete Task")
    print("6️⃣  Filter Tasks by Status")
    print("7️⃣  Exit")

def main():
    while True:
        show_menu()
        choice = input("\n👉 Choose an option: ").strip()

        if choice == "1":
            list_tasks()
        elif choice == "2":
            title = input("\n📌 Enter task title: ").strip()
            description = input("📝 Enter task description (optional): ").strip()
            due_date = input("📅 Enter due date (YYYY-MM-DD): ").strip()
            create_task(title, description, due_date)
        elif choice == "3":
            task_id = input("\n🔎 Enter Task ID to view: ").strip()
            view_task(task_id)
        elif choice == "4":
            task_id = input("\n🔄 Enter Task ID to update: ").strip()
            status = input("✔️ Mark as completed? (yes/no): ").strip().lower() == "yes"
            update_task(task_id, status)
        elif choice == "5":
            task_id = input("\n🗑 Enter Task ID to delete: ").strip()
            delete_task(task_id)
        elif choice == "6":
            status = input("\n🔍 Filter by status (completed/pending): ").strip().lower()
            if status in ["completed", "pending"]:
                filter_tasks(status)
            else:
                print("\n❌ Invalid choice. Please enter 'completed' or 'pending'.")
        elif choice == "7":
            print("\n👋 Exiting... Have a great day!")
            break
        else:
            print("\n❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
