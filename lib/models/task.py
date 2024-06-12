from db import get_db

class Task:
    def __init__(self, id=None, project_id=None, task_name=None, description=None, status='pending', deadline=None):
        self.id = id
        self.project_id = project_id
        self.task_name = task_name
        self.description = description
        self.status = status
        self.deadline = deadline

    def save(self):
        conn = get_db()
        cursor = conn.cursor()
        
        if self.id is None:
            cursor.execute("""
            INSERT INTO tasks (project_id, task_name, description, status, deadline) 
            VALUES (?, ?, ?, ?, ?)
            """, (self.project_id, self.task_name, self.description, self.status, self.deadline))
            self.id = cursor.lastrowid
        else:
            cursor.execute("""
            UPDATE tasks SET project_id = ?, task_name = ?, description = ?, status = ?, deadline = ? WHERE id = ?
            """, (self.project_id, self.task_name, self.description, self.status, self.deadline, self.id))
        
        conn.commit()
        conn.close()

    @classmethod
    def get(cls, task_id):
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return cls(id=row["id"], project_id=row["project_id"], task_name=row["task_name"], description=row["description"], status=row["status"], deadline=row["deadline"])
        return None

    @classmethod
    def delete(cls, task_id):
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()
