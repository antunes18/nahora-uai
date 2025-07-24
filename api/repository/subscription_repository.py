from sqlalchemy.orm import Session
from api.models.subscription import Subscription
from typing import List


class SubscriptionRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, subscription: Subscription) -> Subscription:
        self.session.add(subscription)
        self.session.commit()
        self.session.refresh(subscription)

        return subscription

    def get_all(self, skip: int, limit: int) -> List[Subscription]:
        return self.session.query(Subscription).offset(skip).limit(limit).all()

    def get_one(self, subscription_id: int) -> Subscription:
        return self.session.query(Subscription).filter(Subscription.id == subscription_id).first()

    def update(self, update_subscription: Subscription) -> None:
        self.session.commit()
        self.session.refresh(update_subscription)

    def delete(self, subscription: Subscription) -> None:
        self.session.delete(subscription)
        self.session.commit()
