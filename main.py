# COMMAND ----------
from src.ecommerce.users import User
from src.ecommerce.category import Category
from src.ecommerce.product import Product


print("----- USER -----")

user1 = User("Aditya", "aditya@gmail.com")
user1.show()


print("\n----- CATEGORY -----")

category1 = Category("Electronics", "Electronic items")
category1.show()


print("\n----- PRODUCT -----")

product1 = Product("iPhone 15", 999, category1)
product1.show()
