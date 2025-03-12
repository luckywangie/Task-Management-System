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
