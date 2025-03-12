from sqlalchemy.orm import Session
from lib.db.models import SessionLocal
from lib.db.crud import create_task
from datetime import date

# Function to seed the database
def seed_database():
    db: Session = SessionLocal()

    tasks = [
        {"title": "Learn Python", "description": "Complete Python basics", "due_date": date(2025, 3, 15)},
        {"title": "Build CLI App", "description": "Create a CLI for task management", "due_date": date(2025, 3, 20)},
        {"title": "Read SQLAlchemy Docs", "description": "Learn about ORM and migrations", "due_date": date(2025, 3, 25)},
        {"title": "Plan Project Structure", "description": "Design the architecture for the app", "due_date": date(2025, 3, 30)},
    ]

    for task in tasks:
        create_task(db, task["title"], task["description"], task["due_date"])

    db.close()
    print("✅ Database seeded successfully!")

if __name__ == "__main__":
    seed_database()
