from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime, UTC

from api.core.database import Base


class Subscription(Base):
    __tablename__ = 'subscriptions'
    id: Integer = Column(Integer, primary_key=True)
    status: String = Column(String, nullable=False)
    start_date: DateTime = Column(DateTime, default=datetime.now(UTC))
    end_date: DateTime = Column(DateTime)

    tenant_id: Integer = Column(ForeignKey("tenants.id"))
    plan_id: Integer = Column(ForeignKey("plans.id"))
