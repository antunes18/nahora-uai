import pytest
from typing import List
from sqlalchemy.orm import Session

from test.factories.invoice_factory import InvoiceFactory

from api.models.invoice import Invoice
from api.models.dto.invoice_dto import InvoiceCreateDTO, InvoiceResponseDTO, InvoiceUpdateDTO


@pytest.fixture
def mock_invoice():
    return InvoiceFactory.create()


@pytest.fixture
def mock_invoice_create():
    return InvoiceFactory.dto()


@pytest.fixture
def mock_invoice_update():
    return InvoiceFactory.update_dto()


@pytest.fixture
def mock_invoice_list():
    return InvoiceFactory.create_batch()


@pytest.fixture()
def test_invoice(db_session_for_test: Session, mock_invoice_list: List[Invoice]):
    """
    Cria um utilizador na base de dados para fins de teste.
    """

    for invoice in mock_invoice_list:
        db_session_for_test.add(invoice)
        db_session_for_test.commit()

    return mock_invoice_list


@pytest.fixture
def create_invoice_json():
    return InvoiceFactory.create_json()


@pytest.fixture
def update_invoice_json():
    return InvoiceFactory.update_json()
