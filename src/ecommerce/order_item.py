# COMMAND ----------
from __future__ import annotations
import uuid
from .product import Product


class OrderItem:
    def __init__(self, product: Product, quantity: int, unit_price: float):
        # unique order_item id
        self.id = str(uuid.uuid4())

        # what product was bought
        self.product = product

        # how many units
        self.quantity = quantity

        # price locked at order time (important!)
        self.unit_price = unit_price

    def line_total(self) -> float:
        return self.quantity * self.unit_price

    def show(self) -> None:
        print("\n----- ORDER ITEM -----")
        print("OrderItem ID:", self.id)
        print("Product:", self.product.name)
        print("Quantity:", self.quantity)
        print("Unit Price:", self.unit_price)
        print("Line Total:", self.line_total())
