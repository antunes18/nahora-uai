from typing import List
from unittest.mock import Mock

from api.models.dto.invoice_dto import InvoiceResponseDTO, InvoiceUpdateDTO
from api.models.invoice import Invoice
from api.services.invoice_services import InvoiceService

from test.factories.base import BaseMVCTestFactory

from test.dependencies import (
    mock_invoice_services,
    mock_invoice_repo,
    mock_subscription_repo
)

from test.mocks.invoice import (
    mock_invoice,
    mock_invoice_create,
    mock_invoice_list,
    mock_invoice_update,
)


class TestinvoiceServices(BaseMVCTestFactory):

    def test_get_all(self, mock_invoice_list: List[InvoiceResponseDTO], mock_invoice_services: InvoiceService, mock_invoice_repo: Mock):
        mock_invoice_repo.get_all.return_value = mock_invoice_list
        response = mock_invoice_services.get_all(skip=0, limit=100)

        assert response is not None
        assert len(response) == len(mock_invoice_list)

    def test_get_one(self, mock_invoice: Invoice, mock_invoice_services: InvoiceService, mock_invoice_repo: Mock):
        mock_invoice_repo.get_one.return_value = mock_invoice

        response: Invoice = mock_invoice_services.get_one(1)

        assert response is not None
        assert response == mock_invoice

    def test_create(self, mock_invoice: Invoice, mock_invoice_services: InvoiceService, mock_invoice_repo: Mock):

        mock_invoice_repo.create.return_value = mock_invoice

        response = mock_invoice_services.create(mock_invoice)

        assert response is not None
        assert response == mock_invoice

    def test_update(self, mock_invoice: Invoice, mock_invoice_update: InvoiceUpdateDTO,  mock_invoice_services: InvoiceService, mock_invoice_repo: Mock):
        mock_invoice_repo.get_one.return_value = mock_invoice
        mock_invoice_repo.update.return_value = (
            mock_invoice_update
        )

        response = mock_invoice_services.update(
            mock_invoice.id, mock_invoice_update
        )

        assert response is not None
        assert response == mock_invoice_update

    def test_delete(self, mock_invoice: Invoice, mock_invoice_update: InvoiceUpdateDTO,  mock_invoice_services: InvoiceService, mock_invoice_repo: Mock):
        mock_invoice_repo.get_one.return_value = mock_invoice
        mock_invoice_repo.delete.return_value = None

        response = mock_invoice_services.delete(mock_invoice.id)

        assert response is None
