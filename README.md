Task Management System (Python CLI + SQLAlchemy ORM)
Overview
The Task Management System is a Python-based CLI (Command Line Interface) application designed to help users create, manage, and track tasks efficiently. It leverages SQLAlchemy ORM for database interactions, providing a structured and scalable solution for task management.

Users can perform operations such as creating accounts, adding tasks, editing task details, and tracking task progress. The system ensures data integrity through relationships between users and tasks.

Features
User Management
Create a new user
List all users
Find a user by name
Edit user details
Delete a user and all their associated tasks
Task Management
Create a new task for a specific user
List all tasks for a user
Find a task by title
Edit task details (title, description, due date, and status)
Delete a task
Data Integrity & Validation
Enforces unique usernames
Restricts task statuses to Pending, In Progress, or Completed
Ensures valid date formats for task due dates
Prevents operations on non-existent users or tasks
Technologies Used
Python – Core language for the CLI
SQLAlchemy – ORM for database management
SQLite – Lightweight database for persistent storage
Project Structure
pgsql
Copy
Edit
Task-Management-System/
│── task_manager/
│   ├── __init__.py
│   ├── database.py
│   ├── models.py
│   ├── task_manager.py
│── main.py
│── requirements.txt
│── README.md
database.py – Configures the database connection
models.py – Defines User and Task models using SQLAlchemy
task_manager.py – Implements business logic for user and task operations
main.py – Runs the CLI interface
Setup & Installation
Clone the Repository
sh
Copy
Edit
git clone https://github.com/your-username/Task-Management-System.git
cd Task-Management-System
Create and Activate a Virtual Environment
sh
Copy
Edit
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
Initialize the Database
sh
Copy
Edit
python -c "from task_manager.database import Base, engine; Base.metadata.create_all(engine)"
Run the Application
sh
Copy
Edit
python main.py
Usage Instructions
Upon running the program, the CLI menu will be displayed:

markdown
Copy
Edit
========================================
 Task Management System
========================================
1. Create User
2. List Users
3. Find User
4. Edit User
5. Delete User
6. Create Task
7. List Tasks for a User
8. Find Task by Title
9. Edit Task
10. Delete Task
0. Exit
========================================
Enter your choice:
Follow the on-screen prompts to manage users and tasks efficiently.

Project Requirements Compliance
Requirement	Status
Uses an ORM for database management	 Yes (SQLAlchemy)
Includes at least 2 model classes	 Yes (User & Task)
Implements one-to-many relationships	 Yes (One User → Many Tasks)
Provides property methods with constraints	 Yes
Includes ORM methods for create, delete, and find operations	 Yes
Displays a CLI menu with interactive options	 Yes
Uses loops to keep the user in the application	 Yes
Validates user inputs and provides informative errors	 Yes
Follows OOP best practices	 Yes
Organized file and module structure	 Yes
Includes a requirements.txt with dependencies	 Yes
README.md describing the application	 Yes
License
This project is open-source and available for modification and distribution under the MIT License.

Contributing
Contributions are welcome! If you would like to improve this project, follow these steps:

Fork the Repository
Create a New Branch (git checkout -b feature-branch)
Commit Your Changes (git commit -m "Add new feature")
Push to the Branch (git push origin feature-branch)
Open a Pull Request
Author
Developed by Abdullahi

For any questions or improvements, feel free to reach out.