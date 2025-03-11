from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Define the database URL (using SQLite for simplicity)
DATABASE_URL = "sqlite:///task_manager.db"

# Create the engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Function to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
