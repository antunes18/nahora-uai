from typing import List

from api.repository.invoice_repository import InvoiceRepository
from api.repository.subscription_repository import SubscriptionRepository

from api.models.invoice import Invoice
from api.models.dto.invoice_dto import InvoiceCreateDTO, InvoiceResponseDTO, InvoiceUpdateDTO


class InvoiceService:
    def __init__(
        self, invoice_repo: InvoiceRepository,
        subscription_repo: SubscriptionRepository
    ) -> None:
        self.invoice_repo = invoice_repo
        self.subscription_repo = subscription_repo

    def create(self, dto: InvoiceUpdateDTO) -> Invoice:

        invoice: Invoice = Invoice(
            status=dto.status,
            due_time=dto.due_time,
            paid_date=dto.paid_date,
            subscription_id=1

        )

        return self.invoice_repo.create(invoice)

    def get_all(self, skip: int, limit: int) -> List[Invoice]:
        return self.invoice_repo.get_all(skip=skip, limit=limit)

    def get_one(self, invoice_id: int) -> Invoice:
        return self.invoice_repo.get_one(invoice_id=invoice_id)

    def update(self, invoice_id: int, update_invoice: Invoice):
        old_invoice: Invoice = self.invoice_repo.get_one(invoice_id=invoice_id)

        if not old_invoice:
            # TODO: Implementar Exception
            raise NotImplementedError("EXCEPTION ENTITY NOT FOUND")

        try:
            old_invoice.status = update_invoice.status
            old_invoice.due_time = update_invoice.due_time
            old_invoice.paid_date = update_invoice.paid_date
            old_invoice.subscription_id = update_invoice.subscription_id
            return self.invoice_repo.update(invoice_id=invoice_id, update_invoice=update_invoice)

        except Exception:
            # TODO: Implementar Exception
            raise NotImplementedError("EXCEPTION ENTITY NOT PROCESS")

    def delete(self, invoice_id: int):
        invoice: Invoice = self.invoice_repo.get_one(invoice_id=invoice_id)

        if not invoice:
            # TODO: Implementar Exception
            raise NotImplementedError("EXCEPTION ENTITY NOT FOUND")

        return self.invoice_repo.delete(invoice=invoice)
