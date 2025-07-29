import pytest
from sqlalchemy.orm import Session

from test.factories.plan_factory import PlanTestFactory


@pytest.fixture
def mock_plan():
    return PlanTestFactory.create()


@pytest.fixture
def mock_plan_create():
    return PlanTestFactory.dto()


@pytest.fixture
def mock_plan_update():
    return PlanTestFactory.update_dto()


@pytest.fixture
def mock_plan_list():
    return PlanTestFactory.create_batch()


@pytest.fixture
def test_plan(db_session_for_test: Session, mock_plan_list):
    """
    Cria um utilizador na base de dados para fins de teste.
    """

    for plan in mock_plan_list:
        db_session_for_test.add(plan)
        db_session_for_test.commit()

    return mock_plan_list


@pytest.fixture
def create_plan_json():
    return PlanTestFactory.create_json()


@pytest.fixture
def update_plan_json():
    return PlanTestFactory.update_json()
