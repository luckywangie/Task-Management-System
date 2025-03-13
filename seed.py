from task_manager.database import SessionLocal
from task_manager.models import User, Task
from datetime import date

# Create a new session
session = SessionLocal()

# Sample users
users = [
    User(name="Alice"),
    User(name="Bob"),
    User(name="Charlie"),
    User(name="David"),
    User(name="Emma"),
    User(name="Fiona"),
]

# Add users to session
session.add_all(users)
session.commit()

# Retrieve users from database
alice = session.query(User).filter_by(name="Alice").first()
bob = session.query(User).filter_by(name="Bob").first()
charlie = session.query(User).filter_by(name="Charlie").first()
david = session.query(User).filter_by(name="David").first()
emma = session.query(User).filter_by(name="Emma").first()
fiona = session.query(User).filter_by(name="Fiona").first()

# Sample tasks
tasks = [
    Task(title="Buy groceries", description="Milk, Eggs, Bread", due_date=date(2025, 3, 15), status="Pending", user_id=alice.id),
    Task(title="Complete project", description="Finish React app", due_date=date(2025, 3, 20), status="In Progress", user_id=bob.id),
    Task(title="Workout", description="Gym session at 6 PM", due_date=date(2025, 3, 14), status="Pending", user_id=charlie.id),
    Task(title="Submit report", description="Quarterly financial report", due_date=date(2025, 3, 18), status="Not Started", user_id=david.id),
    Task(title="Fix bug #123", description="Resolve login issue in the backend", due_date=date(2025, 3, 16), status="In Progress", user_id=emma.id),
    Task(title="Plan weekend trip", description="Book flights and hotels", due_date=date(2025, 3, 22), status="Not Started", user_id=fiona.id),
    Task(title="Team meeting", description="Discuss new sprint goals", due_date=date(2025, 3, 13), status="Completed", user_id=alice.id),
    Task(title="Read book", description="Finish reading 'Clean Code'", due_date=date(2025, 3, 25), status="Pending", user_id=bob.id),
    Task(title="Update resume", description="Add latest work experience", due_date=date(2025, 3, 28), status="Not Started", user_id=charlie.id),
    Task(title="Pay electricity bill", description="Due this week", due_date=date(2025, 3, 12), status="Completed", user_id=david.id),
]

# Add tasks to session
session.add_all(tasks)
session.commit()

# Close session
session.close()

print("✅ Database seeded successfully!")
