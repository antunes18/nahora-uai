from logging import disable
from api.models.enums import roles
from sqlalchemy import select
from sqlalchemy.orm import Session
from api.models.subscription import Subscription


class SubscriptionRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, subscription: Subscription) -> Subscription:
        NotImplementedError("Create Not NotImplemented")

    def get_all(self) -> list(Subscription):
        NotImplementedError(
            "GET ALL 'NEED AVALIATION OF SCOPE' not NotImplemented")

    def get_one(self, subscription_id: int) -> Subscription:
        NotImplementedError("GET ONE NotImplemented")

    def update(self, subscription_id: int, update_subscription: Subscription):
        NotImplementedError(
            "UPDATE 'NEED AVALIATION OF SCOPE' not NotImplemented")

    def delete(self, subscription_id: int):
        NotImplementedError("DELETE NotImplemented")
