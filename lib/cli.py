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

def edit_task(task_id):
    """Edit task details (title, description, due date)."""
    conn = connect_db()
    cursor = conn.cursor()
    
    # Fetch existing task
    cursor.execute("SELECT title, description, due_date FROM tasks WHERE id = ?", (task_id,))
    task = cursor.fetchone()

    if not task:
        print("\n❌ Task not found.")
        conn.close()
        return

    print("\n✏️ Editing Task Details (Press Enter to keep existing values)")
    
    new_title = input(f"📌 New Title [{task[0]}]: ").strip() or task[0]
    new_description = input(f"📝 New Description [{task[1]}]: ").strip() or task[1]
    new_due_date = input(f"📅 New Due Date (YYYY-MM-DD) [{task[2]}]: ").strip() or task[2]

    cursor.execute("UPDATE tasks SET title = ?, description = ?, due_date = ? WHERE id = ?", 
                   (new_title, new_description, new_due_date, task_id))
    conn.commit()
    conn.close()
    
    print("\n✅ Task details updated successfully!")

def update_task(task_id):
    """Update task completion status or edit details."""
    print("\n🔄 What would you like to update?")
    print("1️⃣  Edit Task Details (Title, Description, Due Date)")
    print("2️⃣  Mark as Completed/Pending")
    choice = input("\n👉 Choose an option: ").strip()

    if choice == "1":
        edit_task(task_id)
    elif choice == "2":
        conn = connect_db()
        cursor = conn.cursor()
        status = input("✔️ Mark as completed? (yes/no): ").strip().lower() == "yes"
        cursor.execute("UPDATE tasks SET completed = ? WHERE id = ?", (status, task_id))
        conn.commit()
        conn.close()
        print("\n✅ Task status updated successfully!")
    else:
        print("\n❌ Invalid choice. Please try again.")

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
    print("4️⃣  Update Task (Edit or Change Status)")
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
            update_task(task_id)
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
