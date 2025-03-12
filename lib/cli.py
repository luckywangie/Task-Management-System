import sqlite3

DB_PATH = "lib/db/database.db"

def connect_db():
    """Connect to SQLite database."""
    return sqlite3.connect(DB_PATH)

def create_task():
    """Add a new task to the database, allowing users to go back at any step."""
    print("\n[ Add New Task ]  (Type 'back' anytime to cancel)")

    while True:
        title = input("\nEnter task title: ").strip()
        if title.lower() == "back":
            print("\nReturning to the main menu...")
            return
        
        description = input("Enter task description (optional): ").strip()
        if description.lower() == "back":
            print("\nReturning to the main menu...")
            return
        
        due_date = input("Enter due date (YYYY-MM-DD): ").strip()
        if due_date.lower() == "back":
            print("\nReturning to the main menu...")
            return

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (title, description, due_date, completed) VALUES (?, ?, ?, ?)", 
                       (title, description, due_date, False))
        conn.commit()
        conn.close()
        
        print("\nTask added successfully!")
        return

def list_tasks():
    """List all tasks from the database using an index-based system."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT title, due_date, completed FROM tasks ORDER BY id")
    tasks = cursor.fetchall()
    conn.close()

    print("\nTasks:")
    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):  # Generate display index dynamically
            status = "Completed" if task[2] else "Pending"
            print(f"{index}. {task[0]} (Due: {task[1]}) - {status}")
    print("\n")

def get_task_by_index(index):
    """Retrieve the actual database task ID using its display index."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM tasks ORDER BY id")
    tasks = cursor.fetchall()
    conn.close()

    if 1 <= index <= len(tasks):  # Ensure the index is valid
        return tasks[index - 1][0]  # Return the actual task ID
    else:
        return None

def view_task():
    """View details of a specific task using display index."""
    while True:
        try:
            task_index = input("\nEnter task number to view (or type 'back' to cancel): ").strip()
            if task_index.lower() == "back":
                return
            
            task_index = int(task_index)
            task_id = get_task_by_index(task_index)

            if not task_id:
                print("\nInvalid task number. Please try again.")
                continue

            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
            task = cursor.fetchone()
            conn.close()

            if task:
                status = "Completed" if task[4] else "Pending"
                print("\nTask Details:")
                print(f"Title: {task[1]}\nDescription: {task[2]}\nDue Date: {task[3]}\nStatus: {status}\n")
            return
        except ValueError:
            print("\nInvalid input. Please enter a valid task number.")

def edit_task(task_id):
    """Edit task details (title, description, due date)."""
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT title, description, due_date FROM tasks WHERE id = ?", (task_id,))
    task = cursor.fetchone()

    if not task:
        print("\nTask not found.")
        conn.close()
        return

    print("\nEdit Task (Press Enter to keep existing values)")
    new_title = input(f"New Title [{task[0]}]: ").strip() or task[0]
    new_description = input(f"New Description [{task[1]}]: ").strip() or task[1]
    new_due_date = input(f"New Due Date (YYYY-MM-DD) [{task[2]}]: ").strip() or task[2]

    cursor.execute("UPDATE tasks SET title = ?, description = ?, due_date = ? WHERE id = ?", 
                   (new_title, new_description, new_due_date, task_id))
    conn.commit()
    conn.close()
    
    print("\nTask details updated successfully!")

def update_task():
    """Update task completion status or edit details."""
    while True:
        try:
            task_index = input("\nEnter task number to update (or type 'back' to cancel): ").strip()
            if task_index.lower() == "back":
                return

            task_index = int(task_index)
            task_id = get_task_by_index(task_index)

            if not task_id:
                print("\nInvalid task number. Please try again.")
                continue

            while True:
                print("\nUpdate Task:")
                print("1. Edit Task Details")
                print("2. Mark as Completed/Pending")
                print("3. Back")
                
                choice = input("\nChoose an option: ").strip()

                if choice == "1":
                    edit_task(task_id)
                    return
                elif choice == "2":
                    conn = connect_db()
                    cursor = conn.cursor()
                    status = input("Mark as completed? (yes/no): ").strip().lower() == "yes"
                    cursor.execute("UPDATE tasks SET completed = ? WHERE id = ?", (status, task_id))
                    conn.commit()
                    conn.close()
                    print("\nTask status updated successfully!")
                    return
                elif choice == "3":
                    return  
                else:
                    print("\nInvalid choice. Please try again.")
        except ValueError:
            print("\nInvalid input. Please enter a valid task number.")

def delete_task():
    """Delete a task using its display index."""
    while True:
        try:
            task_index = input("\nEnter task number to delete (or type 'back' to cancel): ").strip()
            if task_index.lower() == "back":
                return

            task_index = int(task_index)
            task_id = get_task_by_index(task_index)

            if not task_id:
                print("\nInvalid task number. Please try again.")
                continue

            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            conn.commit()
            conn.close()

            print("\nTask deleted successfully!")
            return
        except ValueError:
            print("\nInvalid input. Please enter a valid task number.")

def filter_tasks():
    """Filter tasks by completion status."""
    while True:
        status = input("\nFilter by status (completed/pending or 'back' to cancel): ").strip().lower()
        if status == "back":
            return
        if status in ["completed", "pending"]:
            conn = connect_db()
            cursor = conn.cursor()
            completed_status = True if status == "completed" else False
            cursor.execute("SELECT title, due_date FROM tasks WHERE completed = ?", (completed_status,))
            tasks = cursor.fetchall()
            conn.close()

            print(f"\n{status.capitalize()} Tasks:")
            if not tasks:
                print("No tasks found.")
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task[0]} (Due: {task[1]})")
            print("\n")
            return
        else:
            print("\nInvalid choice. Please enter 'completed' or 'pending'.")

def show_menu():
    """Display the menu."""
    print("\nTask Management System")
    print("1. List Tasks")
    print("2. Add Task")
    print("3. View Task Details")
    print("4. Update Task (Edit or Change Status)")
    print("5. Delete Task")
    print("6. Filter Tasks by Status")
    print("7. Exit")

def main():
    print("\nWelcome to the Task Management System!")

    while True:
        show_menu()
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            list_tasks()
        elif choice == "2":
            create_task()
        elif choice == "3":
            view_task()
        elif choice == "4":
            update_task()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            filter_tasks()
        elif choice == "7":
            print("\nExiting... Thank you for using the Task Management System!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
