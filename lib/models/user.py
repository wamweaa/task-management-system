from db import get_db
class User:
    def __init__(self,id=None,username=None,role=None,created_at=None):
        self.id = id
        self.username = username
        self.role = role
        self.created_at = created_at
    def save(self):
        conn = get_db()
        cursor = conn.cursor()
        if self.id is None:
         cursor.execute("""
            INSERT INTO users(username,role) VALUES(?,?)
        """,(self.username,self.role))
         id = cursor.lastrowid
        
        else:
            cursor.execute("""
                UPDATE users SET username = ? , role = ? WHERE id = ?
            """,(self.role,self.username,self.id))
            conn.commit()
            conn.close()