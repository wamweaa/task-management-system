# cli.py

import argparse
from lib.helper import (
    init_db,
    create_user,
    list_users,
    create_project,
    list_projects,
    create_task,
    list_tasks,
    delete_user,
    delete_project,
    delete_task
)

def main():
    parser = argparse.ArgumentParser(description="Task Management CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Init DB Command
    parser_init_db = subparsers.add_parser('init_db', help='Initialize the database')
    parser_init_db.set_defaults(func=init_db)

    # Create User Command
    parser_create_user = subparsers.add_parser('create_user', help='Create a new user')
    parser_create_user.add_argument('username', type=str, help='Username of the user')
    parser_create_user.add_argument('role', type=str, help='Role of the user')
    parser_create_user.set_defaults(func=lambda args: create_user(args.username, args.role))

    # List Users Command
    parser_list_users = subparsers.add_parser('list_users', help='List all users')
    parser_list_users.set_defaults(func=lambda args: [print(f"ID: {user['id']}, Username: {user['username']}, Role: {user['role']}") for user in list_users()])

    # Delete User Command
    parser_delete_user = subparsers.add_parser('delete_user', help='Delete a user')
    parser_delete_user.add_argument('user_id', type=int, help='ID of the user to delete')
    parser_delete_user.set_defaults(func=lambda args: delete_user(args.user_id))

    # Create Project Command
    parser_create_project = subparsers.add_parser('create_project', help='Create a new project')
    parser_create_project.add_argument('user_id', type=int, help='ID of the user')
    parser_create_project.add_argument('project_name', type=str, help='Name of the project')
    parser_create_project.add_argument('description', type=str, help='Description of the project')
    parser_create_project.add_argument('deadline', type=str, help='Deadline of the project (YYYY-MM-DD)')
    parser_create_project.set_defaults(func=lambda args: create_project(args.user_id, args.project_name, args.description, args.deadline))

    # List Projects Command
    parser_list_projects = subparsers.add_parser('list_projects', help='List all projects')
    parser_list_projects.set_defaults(func=lambda args: [print(f"ID: {project['id']}, User ID: {project['user_id']}, Project Name: {project['project_name']}") for project in list_projects()])

    # Delete Project Command
    parser_delete_project = subparsers.add_parser('delete_project', help='Delete a project')
    parser_delete_project.add_argument('project_id', type=int, help='ID of the project to delete')
    parser_delete_project.set_defaults(func=lambda args: delete_project(args.project_id))

    # Create Task Command
    parser_create_task = subparsers.add_parser('create_task', help='Create a new task')
    parser_create_task.add_argument('project_id', type=int, help='ID of the project')
    parser_create_task.add_argument('task_name', type=str, help='Name of the task')
    parser_create_task.add_argument('description', type=str, help='Description of the task')
    parser_create_task.add_argument('status', type=str, choices=['pending', 'in-progress', 'completed'], help='Status of the task')
    parser_create_task.add_argument('deadline', type=str, help='Deadline of the task (YYYY-MM-DD)')
    parser_create_task.set_defaults(func=lambda args: create_task(args.project_id, args.task_name, args.description, args.status, args.deadline))

    # List Tasks Command
    parser_list_tasks = subparsers.add_parser('list_tasks', help='List all tasks')
    parser_list_tasks.set_defaults(func=lambda args: [print(f"ID: {task['id']}, Project ID: {task['project_id']}, Task Name: {task['task_name']}") for task in list_tasks()])

    # Delete Task Command
    parser_delete_task = subparsers.add_parser('delete_task', help='Delete a task')
    parser_delete_task.add_argument('task_id', type=int, help='ID of the task to delete')
    parser_delete_task.set_defaults(func=lambda args: delete_task(args.task_id))

    args = parser.parse_args()
    if args.command == 'init_db':
        args.func()  # Call init_db without arguments
    elif hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
