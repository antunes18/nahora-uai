from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime

from api.core.database import Base


class Invoice(Base):
    __tablename__ = "invoices"
    id: Integer = Column(Integer, primary_key=True, autoincrement=True)
    status: String = Column(String)
    due_time: DateTime = Column(DateTime, default=datetime.now(datetime.UTC))
    paid_date: DateTime = Column(DateTime)

    subscription_id: Integer = Column(ForeignKey("subscriptions.id"))
