from db import get_db

class User:
    def __init__(self, id=None, username=None, role=None, created_at=None):
        self.id = id
        self.username = username
        self.role = role
        self.created_at = created_at

    def save(self):
        conn = get_db()
        cursor = conn.cursor()
        
        if self.id is None:
            cursor.execute("""
            INSERT INTO users (username, role) 
            VALUES (?, ?)
            """, (self.username, self.role))
            self.id = cursor.lastrowid
        else:
            cursor.execute("""
            UPDATE users SET username = ?, role = ? WHERE id = ?
            """, (self.username, self.role, self.id))
        
        conn.commit()
        conn.close()

    @classmethod
    def get(cls, user_id):
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return cls(id=row["id"], username=row["username"], role=row["role"], created_at=row["created_at"])
        return None

    @classmethod
    def delete(cls, user_id):
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        conn.close()
