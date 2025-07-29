from datetime import datetime
from typing import List

from api.exceptions.generics import EntityNotFound, EntityAlreadyExists, InvalidData, FieldAlreadyUsed

from api.models.invoice import Invoice
from api.models.dto.invoice_dto import InvoiceCreateDTO, InvoiceResponseDTO, InvoiceUpdateDTO
from api.models.enums.invoice_status import InvoiceStatus

from api.repository.invoice_repository import InvoiceRepository
from api.repository.subscription_repository import SubscriptionRepository


class InvoiceService:
    def __init__(
        self, invoice_repo: InvoiceRepository,
        subscription_repo: SubscriptionRepository
    ) -> None:
        self.invoice_repo = invoice_repo
        self.subscription_repo = subscription_repo

    def create(self, dto: InvoiceCreateDTO) -> Invoice:

        self._validate_data(dto)

        invoice: Invoice = Invoice(
            status=InvoiceStatus.pending,
            due_time=dto.due_time,
            paid_date=dto.paid_date,
            subscription_id=dto.subscription_id
        )

        return self.invoice_repo.create(invoice)

    def get_all(self, skip: int, limit: int) -> List[Invoice]:
        return self.invoice_repo.get_all(skip=skip, limit=limit)

    def get_one(self, invoice_id: int) -> Invoice:
        invoice = self.invoice_repo.get_one(invoice_id=invoice_id)

        if not invoice:
            raise EntityNotFound("Invoice")

        return invoice

    def update(self, invoice_id: int, update_invoice: InvoiceUpdateDTO) -> Invoice:
        old_invoice: Invoice = self.invoice_repo.get_one(invoice_id=invoice_id)
        if not old_invoice:
            raise EntityNotFound("Invoice")

        if update_invoice.status not in InvoiceStatus:
            raise InvalidData("Tipo de Status")

        self._validate_data(update_invoice)

        try:
            old_invoice.status = update_invoice.status
            old_invoice.due_time = update_invoice.due_time
            old_invoice.paid_date = update_invoice.paid_date
            old_invoice.subscription_id = update_invoice.subscription_id

            return self.invoice_repo.update(update_invoice=old_invoice)

        except Exception:
            raise InvalidData("Dados de Invoice")

    def delete(self, invoice_id: int) -> None:
        invoice: Invoice = self.invoice_repo.get_one(invoice_id=invoice_id)

        if not invoice:
            raise EntityNotFound("Invoice")

        return self.invoice_repo.delete(invoice=invoice)

    def _validate_data(self, obj: Invoice) -> None:

        # TODO: Precisa de Validação para não gerar 2 Invoice para uma Subscription

        if not self.subscription_repo.get_one(obj.subscription_id):
            raise EntityNotFound("Subscription")

        if obj.due_time.date() < datetime.now().date():
            raise InvalidData(
                "Não é possivel registrar a DATA DE VENCIMENTO para anterior à Data de Hoje! Data"
            )
