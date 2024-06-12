from db import get_db

class Project:
    def __init__(self, id=None, user_id=None, project_name=None, description=None, deadline=None):
        self.id = id
        self.user_id = user_id
        self.project_name = project_name
        self.description = description
        self.deadline = deadline

    def save(self):
        conn = get_db()
        cursor = conn.cursor()
        
        if self.id is None:
            cursor.execute("""
            INSERT INTO projects (user_id, project_name, description, deadline) 
            VALUES (?, ?, ?, ?)
            """, (self.user_id, self.project_name, self.description, self.deadline))
            self.id = cursor.lastrowid
        else:
            cursor.execute("""
            UPDATE projects SET user_id = ?, project_name = ?, description = ?, deadline = ? WHERE id = ?
            """, (self.user_id, self.project_name, self.description, self.deadline, self.id))
        
        conn.commit()
        conn.close()

    @classmethod
    def get(cls, project_id):
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM projects WHERE id = ?", (project_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return cls(id=row["id"], user_id=row["user_id"], project_name=row["project_name"], description=row["description"], deadline=row["deadline"])
        return None

    @classmethod
    def delete(cls, project_id):
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM projects WHERE id = ?", (project_id,))
        conn.commit()
        conn.close()
