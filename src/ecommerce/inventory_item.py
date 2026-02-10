# COMMAND ----------
import uuid

class InventoryItem:

    def __init__(self, product, quantity):
        self.id = str(uuid.uuid4())
        self.product = product
        self.quantity = quantity

    def can_fulfill(self, amount: int) -> bool:
        return amount <= self.quantity

    def add_stock(self, amount):
        self.quantity += amount
        print("Stock added. New quantity:", self.quantity)

    def remove_stock(self, amount):
        if amount > self.quantity:
            print("Not enough stock!")
        else:
            self.quantity -= amount
            print("Stock removed. Remaining quantity:", self.quantity)

    def show(self):
        print("\n----- INVENTORY ITEM -----")
        print("Inventory ID:", self.id)
        print("Product:", self.product.name)
        print("Available Quantity:", self.quantity)
