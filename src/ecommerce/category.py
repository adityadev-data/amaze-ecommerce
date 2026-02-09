# COMMAND ----------
import uuid


class Category:

    def __init__(self, name, description):

        self.id = str(uuid.uuid4())

        self.name = name

        self.description = description

    def show(self):

        print("Category ID:", self.id)
        print("Category Name:", self.name)
        print("Description:", self.description)
