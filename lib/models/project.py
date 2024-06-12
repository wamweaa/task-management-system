from __init__ import CURSOR, CONN

class Project:
    def __init__(self,id,user_id,project_name,description,deadline):
        self.id = id
        self.user_id = user_id
        self.project_name = project_name
        self.description = description
        self.deadline = deadline