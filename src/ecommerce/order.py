# COMMAND ----------
from __future__ import annotations
import uuid
from typing import List

from .cart_item import CartItem
from .order_item import OrderItem


class Order:
    def __init__(self, cart_items: List[CartItem]):
        self.id = str(uuid.uuid4())

        # order lifecycle
        self.status = "CREATED"   # CREATED -> PAID -> SHIPPED -> DELIVERED

        # freeze cart into order items
        self.items: List[OrderItem] = []
        for ci in cart_items:
            self.items.append(OrderItem(ci.product, ci.quantity, ci.product.price))

    def total(self) -> float:
        return sum(item.line_total() for item in self.items)

    def mark_paid(self) -> None:
        if self.status != "CREATED":
            print("Order cannot be marked PAID now. Current status:", self.status)
            return
        self.status = "PAID"
        print("✅ Order marked as PAID")

    def mark_shipped(self) -> None:
        if self.status != "PAID":
            print("Order cannot be marked SHIPPED now. Current status:", self.status)
            return
        self.status = "SHIPPED"
        print("✅ Order marked as SHIPPED")

    def mark_delivered(self) -> None:
        if self.status != "SHIPPED":
            print("Order cannot be marked DELIVERED now. Current status:", self.status)
            return
        self.status = "DELIVERED"
        print("✅ Order marked as DELIVERED")

    def show(self) -> None:
        print("\n===== ORDER =====")
        print("Order ID:", self.id)
        print("Status:", self.status)

        if not self.items:
            print("No items in order")
            return

        print("\nItems:")
        for item in self.items:
            print(f"- {item.product.name} x {item.quantity} = {item.line_total()}")

        print("\nTOTAL =", self.total())
