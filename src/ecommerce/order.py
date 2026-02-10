# COMMAND ----------
import uuid
from typing import List
from src.ecommerce.order_status import OrderStatus
from src.ecommerce.cart_item import CartItem


class Order:

    def __init__(self, items: List[CartItem]):

        self.id = str(uuid.uuid4())

        self.items = items

        self.status = OrderStatus.CREATED


    def total(self):

        return sum(item.line_total() for item in self.items)


    def mark_paid(self):

        self.status = OrderStatus.PAID

        print("✅ Order marked as PAID")


    def mark_shipped(self):

        self.status = OrderStatus.SHIPPED

        print("✅ Order marked as SHIPPED")


    def mark_delivered(self):

        self.status = OrderStatus.DELIVERED

        print("✅ Order marked as DELIVERED")


    def show(self):

        print("\n===== ORDER =====")

        print("Order ID:", self.id)

        print("Status:", self.status.value)

        print("\nItems:")

        for item in self.items:

            print(f"- {item.product.name} x {item.quantity} = {item.line_total()}")

        print("\nTOTAL =", self.total())
