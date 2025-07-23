from api.repository.invoice_repository import InvoiceRepository
from api.repository.subscription_repository import SubscriptionRepository
from api.models.invoice import Invoice


class InvoiceService:
    def __init__(
        self, invoice_repo: InvoiceRepository,
        subscription_repo: SubscriptionRepository
    ):
        self.invoice_repo = invoice_repo
        self.subscription_repo = subscription_repo

    def create(self, dto: Invoice):
        raise NotImplementedError("CREATE Not Implemented")

    def get_all(self):
        raise NotImplementedError("GET ALL Not Implemented")

    def get_one(self, invoice_id: int):
        raise NotImplementedError(" GET ONE Not Implemented")

    def update(self, invoice_id: int, update_invoice: Invoice):
        raise NotImplementedError(" UPDATE Not Implemented")

    def delete(self, invoice_id: int):
        raise NotImplementedError(" DELETE Not Implemented")
