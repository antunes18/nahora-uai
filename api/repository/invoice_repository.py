from logging import disable
from api.models.enums import roles
from sqlalchemy import select
from sqlalchemy.orm import Session
from api.models.invoice import Invoice

from typing import List


class InvoiceRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, invoice: Invoice) -> Invoice:
        self.session.add(invoice)
        self.session.commit()
        self.session.refresh(invoice)

        return invoice

    def get_all(self, skip: int, limit: int) -> List[Invoice]:
        return self.session.query(Invoice).offset(skip).limit(limit).all()

    def get_one(self, invoice_id: int) -> Invoice:
        return self.session.query(Invoice).filter(Invoice.id == invoice_id).first()

    def update(self, invoice_id: int, update_invoice: Invoice):
        old_invoice = self.get_one(invoice_id)

        if old_invoice:
            old_invoice.status = update_invoice.status
            old_invoice.due_time = update_invoice.due_time
            old_invoice.paid_date = update_invoice.paid_date
            old_invoice.subscription_id = update_invoice.subscription_id

            self.session.commit()
            self.session.refresh(old_invoice)

    def delete(self, invoice_id: int):
        NotImplementedError("DELETE NotImplemented")
