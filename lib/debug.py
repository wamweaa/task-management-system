  
from db import init_db
from models.user import User
from models.project import Project
from models.task import Task

def main():
    # Initialize the database
    init_db()

    # Create a new user
    user = User(username="jane_doe", role="manager")
    user.save()
    print(f"Created user: {user}")

    # Fetch the created user
    fetched_user = User.get(user.id)
    print(f"Fetched user: {fetched_user}")

    # Create a new project for the user
    project = Project(user_id=user.id, project_name="Project Beta", description="Second project", deadline="2024-12-31")
    project.save()
    print(f"Created project: {project}")

    # Fetch the created project
    fetched_project = Project.get(project.id)
    print(f"Fetched project: {fetched_project}")

    # Create a new task for the project
    task = Task(project_id=project.id, task_name="Task 2", description="Second task", deadline="2024-11-30")
    task.save()
    print(f"Created task: {task}")

    # Fetch the created task
    fetched_task = Task.get(task.id)
    print(f"Fetched task: {fetched_task}")

if __name__ == "__main__":
    main()
