from logging import disable
from api.models.enums import roles
from sqlalchemy import select
from sqlalchemy.orm import Session
from api.models.subscription import Subscription
from typing import List


class SubscriptionRepository:
    def __init__(self, session: Session):
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

    def update(self, subscription_id: int, update_subscription: Subscription):
        old_subscription: Subscription = self.get_one(
            subscription_id=subscription_id)

        if old_subscription:
            old_subscription.status = update_subscription.status
            old_subscription.start_date = update_subscription.start_date
            old_subscription.end_date = update_subscription.end_date
            old_subscription.tenant_id = update_subscription.tenant_id
            old_subscription.plan_id = update_subscription.plan_id

            self.session.commit()
            self.session.refresh(old_subscription)

    def delete(self, subscription_id: int):
        raise NotImplementedError("DELETE NotImplemented")
