from enum import Enum


class SubscriptionStatus(str, Enum):
    active = "active"
    disable = "disable"
    pending = "pending"
