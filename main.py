# COMMAND ----------
from src.ecommerce.users import User
from src.ecommerce.category import Category
from src.ecommerce.product import Product
from src.ecommerce.inventory_item import InventoryItem
from src.ecommerce.cart import Cart
from src.ecommerce.order import Order
from src.ecommerce.payment import Payment, PaymentMethod
from src.ecommerce.shipment import Shipment


def header(title: str):
    print("\n" + "=" * 10, title, "=" * 10)

header("USER")
user1 = User("Aditya", "aditya@gmail.com")
user1.show()


header("CATEGORY")
category1 = Category("Electronics", "Electronic items")
category1.show()


header("PRODUCT")
product1 = Product("iPhone 15", 999, category1)
product1.show()


header("INVENTORY")
inventory1 = InventoryItem(product1, 10)
inventory1.show()


header("CART")
cart = Cart()
cart.add_item(product1, 2, inventory1)
cart.show()


header("ORDER")
order = Order(cart.items)
order.show()
order.mark_shipped()
order.mark_delivered()


header("PAYMENT")

payment = Payment(order, PaymentMethod.CARD)

payment.show()

payment.process()

payment.show()

header("ORDER AFTER PAYMENT")
order.show()

header("SHIPMENT")

shipment = Shipment(order.id, "845 Burrack Lane, Brampton, ON")
shipment.show()

shipment.mark_shipped()
shipment.show()

shipment.mark_delivered()
shipment.show()




