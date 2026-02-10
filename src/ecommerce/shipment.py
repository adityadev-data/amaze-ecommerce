# COMMAND ----------
import uuid
from enum import Enum


class ShipmentStatus(Enum):
    CREATED = "CREATED"
    SHIPPED = "SHIPPED"
    DELIVERED = "DELIVERED"


class Shipment:

    def __init__(self, order_id: str, address: str):
        self.id = str(uuid.uuid4())
        self.order_id = order_id
        self.address = address
        self.status = ShipmentStatus.CREATED

    def show(self):
        print("\n===== SHIPMENT =====")
        print("Shipment ID:", self.id)
        print("Order ID:", self.order_id)
        print("Address:", self.address)
        print("Status:", self.status.value)

    def mark_shipped(self):
        self.status = ShipmentStatus.SHIPPED
        print("✅ Shipment marked as SHIPPED")

    def mark_delivered(self):
        self.status = ShipmentStatus.DELIVERED
        print("✅ Shipment marked as DELIVERED")
