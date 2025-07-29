from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Enum
from datetime import datetime, UTC

from api.core.database import Base
from api.models.enums.subscription_status import SubscriptionStatus


class Subscription(Base):
    __tablename__ = 'subscriptions'
    id: Integer = Column(Integer, primary_key=True)
    status: SubscriptionStatus = Column(Enum(
        SubscriptionStatus, name="subscription_status"), nullable=False, default=SubscriptionStatus.disable)
    start_date: DateTime = Column(DateTime, default=datetime.now(UTC))
    end_date: DateTime = Column(DateTime)

    tenant_id: Integer = Column(ForeignKey("tenants.id"))
    plan_id: Integer = Column(ForeignKey("plans.id"))
