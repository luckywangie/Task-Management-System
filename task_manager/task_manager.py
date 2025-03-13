from task_manager.database import SessionLocal
from task_manager.models import User, Task
from datetime import datetime

class TaskManager:
    def __init__(self):
        self.session = SessionLocal()

    # 1. Create User
    def create_user(self, username):
        existing_user = self.session.query(User).filter_by(name=username).first()
        if existing_user:
            print(f"User '{username}' already exists.")
        else:
            new_user = User(name=username)
            self.session.add(new_user)
            self.session.commit()
            print(f"User '{username}' created successfully.")

    # 2. List Users
    def list_users(self):
        users = self.session.query(User).all()
        if not users:
            print("No users found.")
            return []
        return [user.name for user in users]

    # 3. Find User
    def find_user(self, username):
        user = self.session.query(User).filter_by(name=username).first()
        return user.name if user else None

    # 4. Edit User
    def edit_user(self, old_name, new_name):
        user = self.session.query(User).filter_by(name=old_name).first()
        if user:
            user.name = new_name
            self.session.commit()
            print(f"User '{old_name}' renamed to '{new_name}'.")
        else:
            print(f"User '{old_name}' not found.")

    # 5. Delete User & Their Tasks (Cascade Delete)
    def delete_user(self, username):
        user = self.session.query(User).filter_by(name=username).first()
        if user:
            self.session.delete(user)
            self.session.commit()
            print(f"User '{username}' and their tasks deleted successfully.")
        else:
            print(f"User '{username}' not found.")

    # 6. Create Task
    def create_task(self, username, title, description, due_date):
        user = self.session.query(User).filter_by(name=username).first()
        if not user:
            print(f"User '{username}' not found.")
            return

        try:
            due_date_obj = datetime.strptime(due_date, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")
            return

        new_task = Task(
            user_id=user.id,
            title=title,
            description=description,
            due_date=due_date_obj,
            status="Pending"
        )
        self.session.add(new_task)
        self.session.commit()
        print(f"Task '{title}' created for user '{username}'.")

    # 7. List Tasks for a User
    def list_tasks(self, username):
        user = self.session.query(User).filter_by(name=username).first()
        if not user:
            print(f"User '{username}' not found.")
            return []

        tasks = self.session.query(Task).filter_by(user_id=user.id).all()
        if not tasks:
            print(f"No tasks found for user '{username}'.")
            return []

        return [
            f"Title: {task.title}, Description: {task.description or 'N/A'}, Due: {task.due_date or 'N/A'}, Status: {task.status}"
            for task in tasks
        ]

    # 8. Find Task by Title
    def find_task(self, title):
        task = self.session.query(Task).filter_by(title=title).first()
        if task:
            return f"Title: {task.title}, Description: {task.description or 'N/A'}, Due: {task.due_date or 'N/A'}, Status: {task.status}"
        return f"Task '{title}' not found."

    # 9. Edit Task
    def edit_task(self, username, title, new_title=None, new_desc=None, new_due=None, new_status=None):
        user = self.session.query(User).filter_by(name=username).first()
        if not user:
            print(f"User '{username}' not found.")
            return

        task = self.session.query(Task).filter_by(user_id=user.id, title=title).first()
        if not task:
            print(f"Task '{title}' not found.")
            return

        if new_title:
            task.title = new_title
        if new_desc:
            task.description = new_desc
        if new_due:
            try:
                task.due_date = datetime.strptime(new_due, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format. Use YYYY-MM-DD.")
                return
        if new_status:
            valid_statuses = {"Pending", "In Progress", "Completed"}
            new_status = new_status.strip().capitalize()  # Normalize input
            if new_status and new_status not in valid_statuses:
                print("Invalid status. Use: Pending, In Progress, or Completed.")
                return
            task.status = new_status

        self.session.commit()
        print(f"Task '{title}' updated successfully.")

    # 10. Delete Task
    def delete_task(self, title):
        task = self.session.query(Task).filter_by(title=title).first()
        if task:
            self.session.delete(task)
            self.session.commit()
            print(f"Task '{title}' deleted successfully.")
        else:
            print(f"Task '{title}' not found.")

