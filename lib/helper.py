# helper.py

from lib.models.user import create_user as create_user_db, list_users as list_users_db
from lib.models.project import create_project as create_project_db, list_projects as list_projects_db
from lib.models.task import create_task as create_task_db, list_tasks as list_tasks_db

def init_db():
    # Initialize the database (create tables, etc.)
    print("Database initialized")

def create_user(args):
    create_user_db(args.username, args.role)
    print(f"User {args.username} created with role {args.role}")

def list_users(args):
    users = list_users_db()
    for user in users:
        print(f"ID: {user['id']}, Username: {user['username']}, Role: {user['role']}")

def create_project(args):
    create_project_db(args.user_id, args.project_name, args.description, args.deadline)
    print(f"Project {args.project_name} created under user ID {args.user_id}")

def list_projects(args):
    projects = list_projects_db()
    for project in projects:
        print(f"ID: {project['id']}, User ID: {project['user_id']}, Project Name: {project['project_name']}")

def create_task(args):
    create_task_db(args.project_id, args.task_name, args.description, args.status, args.deadline)
    print(f"Task {args.task_name} created under project ID {args.project_id}")

def list_tasks(args):
    tasks = list_tasks_db()
    for task in tasks:
        print(f"ID: {task['id']}, Project ID: {task['project_id']}, Task Name: {task['task_name']}")
