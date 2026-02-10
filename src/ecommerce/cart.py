# COMMAND ----------
from __future__ import annotations
from typing import List, Optional
from .cart_item import CartItem
from .product import Product
from .inventory_item import InventoryItem


class Cart:
    def __init__(self):
        self.items: List[CartItem] = []

    def _find_item(self, product_id: str) -> Optional[CartItem]:
        for item in self.items:
            if item.product.id == product_id:
                return item
        return None

    def add_item(self, product: Product, qty: int, inventory: InventoryItem) -> None:
        if qty <= 0:
            raise ValueError("Quantity must be > 0")

        if not inventory.can_fulfill(qty):
            raise ValueError(f"Not enough stock for {product.name}")

        existing = self._find_item(product.id)
        if existing:
            # increase quantity
            inventory.remove_stock(qty)
            existing.quantity += qty
        else:
            inventory.remove_stock(qty)
            self.items.append(CartItem(product, qty))

    def remove_item(self, product_id: str, inventory: InventoryItem) -> None:
        item = self._find_item(product_id)
        if not item:
            return

        # return stock back
        inventory.add_stock(item.quantity)
        self.items = [x for x in self.items if x.product.id != product_id]

    def total(self) -> float:
        return sum(item.line_total() for item in self.items)

    def show(self) -> None:
        print("\n----- CART -----")
        if not self.items:
            print("Cart is empty")
            return

        for item in self.items:
            print(f"{item.product.name} x {item.quantity} = {item.line_total()}")

        print(f"TOTAL = {self.total()}")


