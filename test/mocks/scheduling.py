import pytest
import datetime

from sqlalchemy.orm import Session
from typing import List

from api.models.scheduling import Scheduling
from api.models.user import User
from api.models.tenant import Tenant

from api.models.dto.scheduling_dto import SchedulingCreateDto, SchedulingDTO

from test.factories.scheduling_factory import SchedulingFactory
from test.mocks.user import mock_user

from test.mocks.tenant import mock_tenant


@pytest.fixture
def mock_scheduling():
    return SchedulingFactory.create()


@pytest.fixture
def mock_scheduling_create():
    return SchedulingFactory.dto()


@pytest.fixture
def mock_scheduling_update():
    return SchedulingFactory.update_dto()


@pytest.fixture
def mock_scheduling_list():
    return SchedulingFactory.create_batch()


@pytest.fixture()
def test_scheduling(db_session_for_test: Session, mock_scheduling_list: List[SchedulingDTO]):
    """
    Cria um utilizador na base de dados para fins de teste.
    """

    for scheduling in mock_scheduling_list:
        db_session_for_test.add(scheduling)
        db_session_for_test.commit()

    return mock_scheduling_list


@pytest.fixture
def create_scheduling_json():
    return ({
        "tenant_id": 1,
        "date": "2030-07-16T23:15:36.736Z",
        "hour": 16,
        "name": "client_username",
        "user_id": 1,
        "phone": "1234567891231"

    })


@pytest.fixture
def update_scheduling_json():
    return ({
        "tenant_id": "1",
        "date": "2030-07-16T23:15:36.736Z",
        "hour": 18,
        "name": "update_client_username",
        "user_id": 1,
        "phone": "1234567891231"

    })
