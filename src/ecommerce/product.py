# COMMAND ----------
import uuid


class Product:

    def __init__(self, name, price, category):

        self.id = str(uuid.uuid4())

        self.name = name

        self.price = price

        self.category = category

    def show(self):

        print("Product ID:", self.id)
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Category:", self.category.name)
