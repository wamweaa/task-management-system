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

def create_task(project_id, task_name, description, status, deadline):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (project_id, task_name, description, status, deadline) VALUES (?, ?, ?, ?, ?)", 
                   (project_id, task_name, description, status, deadline))
    conn.commit()
    conn.close()

def list_tasks():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks
