from enum import Enum


class InvoiceStatus(str, Enum):
    paid = "paid"
    pending = "pending"
    canceled = "canceled"
    unpaid = "unpaid"
