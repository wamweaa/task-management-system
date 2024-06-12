import sqlite3

DATABASE_NAME = "task_management.db"

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row

    return conn
def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute( """
    CREATE TABLE IF NOT EXIST users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(100) NOT NULL,
        role VARCHAR(50) NOT NULL,
        created_at TIMESTAMP DEAFAULT CURRENT_TIMESTAMP
    )""" )
    cursor.execute( """
    CREATE TABLE IF NOT EXIST projects(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        projec_name TEXT,
        description VARCHAR(50) NOT NULL,
        deadline DATE,
        FOREIGN_KEY(user_id) REFFERENCES users (id)
    )""" )
    cursor.execute( """
    CREATE TABLE IF NOT EXIST tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER,
        task_name TEXT,
        description VARCHAR(50) NOT NULL,
        status VARCHAR(50) DEFAULT "pending",
        deadline DATE,
        FOREIGN_KEY (project_id) REFFERENCES projects (id)
        
    )""" )
    conn.commit()
    conn.close()