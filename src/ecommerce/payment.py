# COMMAND ----------
import uuid
from .payment_status import PaymentStatus
from .payment_method import PaymentMethod


class Payment:

    def __init__(self, order, method: PaymentMethod):

        self.id = str(uuid.uuid4())

        self.order = order              # store full order object
        self.amount = order.total()     # calculate from order
        self.method = method

        self.status = PaymentStatus.PENDING


    def show(self):

        print("\n===== PAYMENT =====")
        print("Payment ID:", self.id)
        print("Order ID:", self.order.id)
        print("Amount:", self.amount)
        print("Method:", self.method.value)
        print("Status:", self.status.value)


    def process(self):

        # simulate success
        self.status = PaymentStatus.SUCCESS
        print("✅ Payment SUCCESS")

        # ✅ AUTO UPDATE ORDER
        self.order.mark_paid()
