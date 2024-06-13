from .user import create_user, list_users
from .project import create_project, list_projects
from .task import create_task, list_tasks

def init_db():
    # Initialize database by creating tables
    from .user import init_db as init_user_db
    from .project import init_db as init_project_db
    from .task import init_db as init_task_db
    init_user_db()
    init_project_db()
    init_task_db()
