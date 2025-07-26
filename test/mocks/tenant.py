import pytest
from typing import List
from sqlalchemy.orm import Session

from test.factories.tenant_factory import TenantFactory

from api.models.tenant import Tenant
from api.models.dto.tenant_dto import TenantResponseDTO


@pytest.fixture
def mock_tenant():
    return TenantFactory.create()


@pytest.fixture
def mock_tenant_create():
    return TenantFactory.dto()


@pytest.fixture
def mock_tenant_update():
    return TenantFactory.update_dto()


@pytest.fixture
def mock_tenant_list():
    return TenantFactory.create_batch()


@pytest.fixture
def test_tenant(db_session_for_test: Session, mock_tenant_list):
    """
    Cria um utilizador na base de dados para fins de teste.
    """

    for tenant in mock_tenant_list:
        db_session_for_test.add(tenant)
        db_session_for_test.commit()

    return mock_tenant_list


@pytest.fixture()
def create_tenant_json():
    return ({
        "name": "string",
        "subdomain": "string",
        "logo_url": "string",
        "primary_color": "string"
    })


@pytest.fixture()
def update_tenant_json():
    return ({
        "name": "update_name",
        "subdomain": "update_subdomain",
        "logo_url": "update_logo_url",
        "primary_color": "update_primary_color"
    }


    )
