# helper.py

import sqlite3
from lib.models.user import create_user as create_user_db, list_users as list_users_db
from lib.models.project import create_project as create_project_db, list_projects as list_projects_db
from lib.models.task import create_task as create_task_db, list_tasks as list_tasks_db

DATABASE_NAME = "task_management.db"

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        role TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        project_name TEXT NOT NULL,
        description TEXT,
        deadline DATE,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER,
        task_name TEXT NOT NULL,
        description TEXT,
        status TEXT DEFAULT 'pending',
        deadline DATE,
        FOREIGN KEY (project_id) REFERENCES projects (id)
    )
    """)
    
    conn.commit()
    conn.close()

def create_user(username, role):
    create_user_db(username, role)

def list_users():
    return list_users_db()

def create_project(user_id, project_name, description, deadline):
    create_project_db(user_id, project_name, description, deadline)

def list_projects():
    return list_projects_db()

def create_task(project_id, task_name, description, status, deadline):
    create_task_db(project_id, task_name, description, status, deadline)

def list_tasks():
    return list_tasks_db()

def delete_user(user_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()

def delete_project(project_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM projects WHERE id = ?", (project_id,))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
