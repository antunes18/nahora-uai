from api.repository.invoice_repository import InvoiceRepository
from api.models.invoice import Invoice
from api.models.dto.invoice_dto import InvoiceUpdateDTO

from test.factories.base import BaseMVCTestFactory


from test.dependencies import (
    real_invoice_repo
)

from test.mocks.invoice import (
    mock_invoice,
    mock_invoice_create,
    mock_invoice_list,
    mock_invoice_update,
    test_invoice
)


class TestInvoiceRepository(BaseMVCTestFactory):

    def test_create(self, real_invoice_repo: InvoiceRepository, mock_invoice: Invoice):
        data = real_invoice_repo.create(mock_invoice)

        assert data == mock_invoice

    def test_get_all(self, real_invoice_repo: InvoiceRepository, test_invoice):
        data = real_invoice_repo.get_all(skip=0, limit=100)

    def test_get_one(self, real_invoice_repo: InvoiceRepository, test_invoice):
        data = real_invoice_repo.get_one(1)

        assert data == test_invoice[0]

    def test_update(self, real_invoice_repo: InvoiceRepository, mock_invoice: Invoice, mock_invoice_update: InvoiceUpdateDTO):
        mock_invoice.id = 1
        real_invoice_repo.session.add(mock_invoice)
        real_invoice_repo.session.commit()

        original: Invoice = real_invoice_repo.session.get(
            Invoice, mock_invoice.id)

        original.status = mock_invoice_update.status
        original.due_time = mock_invoice_update.due_time
        original.paid_date = mock_invoice_update.paid_date
        original.subscription_id = mock_invoice_update.subscription_id

        data = real_invoice_repo.update(original)

        assert data is not None

        assert data == original

    def test_delete(self, real_invoice_repo: InvoiceRepository, mock_invoice):
        mock_invoice.id = 1
        real_invoice_repo.session.add(mock_invoice)
        real_invoice_repo.session.commit()

        data = real_invoice_repo.delete(mock_invoice)

        assert data is None

        result = real_invoice_repo.get_one(1)

        assert result is None
