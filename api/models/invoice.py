from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Enum
from datetime import datetime, UTC

from api.core.database import Base

from api.models.enums.invoice_status import InvoiceStatus


class Invoice(Base):
    __tablename__ = "invoices"
    id: Integer = Column(Integer, primary_key=True, autoincrement=True)
    status: String = Column(Enum(InvoiceStatus, name="invoice_status"),
                            nullable=False, default=InvoiceStatus.pending)
    due_time: DateTime = Column(DateTime, default=datetime.now(UTC))
    paid_date: DateTime = Column(DateTime)
    subscription_id: Integer = Column(ForeignKey("subscriptions.id"))
