# COMMAND ----------
import uuid

class User:
    def __init__(self, name, email):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email

    def show(self):
        print("User ID:", self.id)
        print("Name:", self.name)
        print("Email:", self.email)