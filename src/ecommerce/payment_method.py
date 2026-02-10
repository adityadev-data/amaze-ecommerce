# COMMAND ----------
from enum import Enum


class PaymentMethod(Enum):
    CARD = "CARD"
    CASH = "CASH"
    UPI = "UPI"