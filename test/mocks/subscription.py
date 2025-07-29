import pytest
from typing import List
from sqlalchemy.orm import Session

from test.factories.subscription_factory import SubscriptionTestFactory


@pytest.fixture
def mock_subscription():
    return SubscriptionTestFactory.create()


@pytest.fixture
def mock_subscription_create():
    return SubscriptionTestFactory.dto()


@pytest.fixture
def mock_subscription_update():
    return SubscriptionTestFactory.update_dto()


@pytest.fixture
def mock_subscription_list():
    return SubscriptionTestFactory.create_batch()


@pytest.fixture
def test_subscription(db_session_for_test: Session, mock_subscription_list):
    """
    Cria um utilizador na base de dados para fins de teste.
    """

    for subscription in mock_subscription_list:
        db_session_for_test.add(subscription)
        db_session_for_test.commit()

    return mock_subscription_list


@pytest.fixture
def create_subscription_json():
    return SubscriptionTestFactory.create_json()


@pytest.fixture
def update_subscription_json():
    return SubscriptionTestFactory.update_json()
