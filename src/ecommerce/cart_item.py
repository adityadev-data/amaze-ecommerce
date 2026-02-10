# COMMAND ----------
from dataclasses import dataclass
from .product import Product

@dataclass
class CartItem:
    product: Product
    quantity: int

    def line_total(self) -> float:
        return self.product.price * self.quantity
