import click
from lib.db.models import SessionLocal, Task

@click.group()
def cli():
    """Task Management CLI"""
    pass

if __name__ == "__main__":
    cli()

#Add a new task 
@cli.command()
@click.option('--title', prompt="Task Title", help="The title of the task")
@click.option('--description', prompt="Task Description", help="A short description of the task")
@click.option('--due-date', prompt="Due Date (YYYY-MM-DD)", help="The due date for the task")
def add(title, description, due_date):
    """Add a new task"""
    session = SessionLocal()
    new_task = Task(title=title, description=description, due_date=due_date, completed=False)
    session.add(new_task)
    session.commit()
    session.close()
    print(f"✅ Task '{title}' added successfully!")

#List all tasks
@cli.command()
def list():
    """List all tasks"""
    session = SessionLocal()
    tasks = session.query(Task).all()
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            status = "✅ Completed" if task.completed else "❌ Pending"
            print(f"{task.id}. {task.title} - {status} (Due: {task.due_date})")
    session.close()

#View a task
@cli.command()
@click.argument('task_id', type=int)
def view(task_id):
    """View details of a task"""
    session = SessionLocal()
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        status = "✅ Completed" if task.completed else "❌ Pending"
        print(f"Title: {task.title}\nDescription: {task.description}\nDue Date: {task.due_date}\nStatus: {status}")
    else:
        print(f"Task with ID {task_id} not found.")
    session.close()

#Update task status
@cli.command()
@click.argument('task_id', type=int)
@click.option('--completed', type=bool, default=True, help="Mark task as completed (True/False)")
def update(task_id, completed):
    """Update a task's status"""
    session = SessionLocal()
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        task.completed = completed
        session.commit()
        print(f"Task '{task.title}' updated to {'Completed' if completed else 'Pending'}.")
    else:
        print(f"Task with ID {task_id} not found.")
    session.close()

#Delete a task
@cli.command()
@click.argument('task_id', type=int)
def delete(task_id):
    """Delete a task"""
    session = SessionLocal()
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        session.delete(task)
        session.commit()
        print(f"Task '{task.title}' deleted successfully!")
    else:
        print(f"Task with ID {task_id} not found.")
    session.close()
