from task_manager.database import Base, engine

# Create tables in the database
Base.metadata.create_all(engine)

print("✅ Database schema created successfully!")
