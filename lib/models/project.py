import sqlite3

DATABASE_NAME = "task_management.db"

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()
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
    conn.commit()
    conn.close()

def create_project(user_id, project_name, description, deadline):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO projects (user_id, project_name, description, deadline) VALUES (?, ?, ?, ?)", 
                   (user_id, project_name, description, deadline))
    conn.commit()
    conn.close()

def list_projects():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM projects")
    projects = cursor.fetchall()
    conn.close()
    return projects
