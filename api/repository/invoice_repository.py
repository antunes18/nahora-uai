from logging import disable
from api.models.enums import roles
from sqlalchemy import select
from sqlalchemy.orm import Session
from api.models.invoice import Invoice


class InvoiceRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, invoice: Invoice) -> Invoice:
        NotImplementedError("Create Not NotImplemented")

    def get_all(self) -> list(Invoice):
        NotImplementedError(
            "GET ALL 'NEED AVALIATION OF SCOPE' not NotImplemented")

    def get_one(self, invoice_id: int) -> Invoice:
        NotImplementedError("GET ONE NotImplemented")

    def update(self, invoice_id: int, update_invoice: Invoice):
        NotImplementedError(
            "UPDATE 'NEED AVALIATION OF SCOPE' not NotImplemented")

    def delete(self, invoice_id: int):
        NotImplementedError("DELETE NotImplemented")
