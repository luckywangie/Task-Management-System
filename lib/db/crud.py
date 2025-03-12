from sqlalchemy.orm import Session
from lib.db.models import Task

# Create a new task
def create_task(db: Session, title: str, description: str = None, due_date=None):
    new_task = Task(title=title, description=description, due_date=due_date)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

# Get all tasks
def get_tasks(db: Session):
    return db.query(Task).all()

# Get a single task by ID
def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

# Update a task
def update_task(db: Session, task_id: int, title=None, description=None, due_date=None, completed=None):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return None

    if title:
        task.title = title
    if description:
        task.description = description
    if due_date:
        task.due_date = due_date
    if completed is not None:
        task.completed = completed

    db.commit()
    db.refresh(task)
    return task

# Delete a task
def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return None
    db.delete(task)
    db.commit()
    return task
