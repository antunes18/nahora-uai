from sqlalchemy.orm import Session
from api.models.invoice import Invoice

from typing import List


class InvoiceRepository:
    def __init__(self, session: Session) -> None:
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

    def update(self, update_invoice: Invoice) -> Invoice:
        self.session.commit()
        self.session.refresh(update_invoice)
        return update_invoice

    def delete(self, invoice: Invoice) -> None:
        self.session.delete(invoice)
        self.session.commit()
