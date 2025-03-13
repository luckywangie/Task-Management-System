import sys
from task_manager.task_manager import TaskManager

class TaskCLI:
    def __init__(self):
        self.manager = TaskManager()

    def show_menu(self):
        print("\nTASK MANAGEMENT SYSTEM")
        print("=" * 40)
        print("1. Create User")
        print("2. List Users")
        print("3. Find User")
        print("4. Edit User")
        print("5. Delete User & Their Tasks")
        print("6. Create Task")
        print("7. List Tasks for a User")
        print("8. Find Task by Title")
        print("9. Edit Task")
        print("10. Delete Task")
        print("0. Exit")
        print("=" * 40)

    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                username = input("Enter user name: ").strip()
                self.manager.create_user(username)

            elif choice == "2":
                users = self.manager.list_users()
                print("\nUsers:")
                for user in users:
                    print(f"- {user}")

            elif choice == "3":
                username = input("Enter user name to find: ").strip()
                user = self.manager.find_user(username)
                print(f"User found: {user}" if user else "User not found.")

            elif choice == "4":
                old_name = input("Enter current user name: ").strip()
                new_name = input("Enter new user name: ").strip()
                self.manager.edit_user(old_name, new_name)

            elif choice == "5":
                username = input("Enter user name to delete: ").strip()
                self.manager.delete_user(username)

            elif choice == "6":
                username = input("Enter user name: ").strip()
                title = input("Enter task title: ").strip()
                description = input("Enter task description: ").strip()
                due_date = input("Enter due date (YYYY-MM-DD): ").strip()
                self.manager.create_task(username, title, description, due_date)

            elif choice == "7":
                username = input("Enter user name: ").strip()
                tasks = self.manager.list_tasks(username)
                for task in tasks:
                    print(task)

            elif choice == "8":
                title = input("Enter task title to search: ").strip()
                task = self.manager.find_task(title)
                print(task if task else "Task not found.")

            elif choice == "9":
                username = input("Enter user name: ").strip()
                title = input("Enter task title to edit: ").strip()
                new_title = input("New title (Enter to keep current): ").strip() or None
                new_desc = input("New description (Enter to keep current): ").strip() or None
                new_due = input("New due date (YYYY-MM-DD, Enter to keep current): ").strip() or None
                new_status = input("New status (Pending/In Progress/Completed, Enter to keep current): ").strip() or None
                self.manager.edit_task(username, title, new_title, new_desc, new_due, new_status)

            elif choice == "10":
                title = input("Enter task title to delete: ").strip()
                self.manager.delete_task(title)

            elif choice == "0":
                print("Exiting...")
                sys.exit()

            else:
                print("Invalid choice. Please enter a number from 0-10.")

if __name__ == "__main__":
    TaskCLI().run()
