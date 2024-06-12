from db import init_db
from models import User, Project, Task

def main():
    # Initialize the database
    init_db()

    # Create a new user
    user = User(username="john_doe", role="admin")
    user.save()

    # Create a new project for the user
    project = Project(user_id=user.id, project_name="Project Alpha", description="First project", deadline="2024-12-31")
    project.save()

    # Create a new task for the project
    task = Task(project_id=project.id, task_name="Task 1", description="First task", deadline="2024-11-30")
    task.save()

    # Fetch and print the created user, project, and task
    print(User.get(user.id))
    print(Project.get(project.id))
    print(Task.get(task.id))

if __name__ == "__main__":
    main()
