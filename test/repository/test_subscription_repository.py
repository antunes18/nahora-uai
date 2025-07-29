from typing import List
from datetime import datetime, timezone

from api.models.subscription import Subscription
from api.models.dto.subscription_dto import SubscriptionCreateDTO, SubscriptionUpdateDTO, SubscriptionResponseDTO

from api.repository.subscription_repository import SubscriptionRepository

from test.dependencies import real_subscription_repo

from test.factories.base import BaseMVCTestFactory
from test.mocks.subscription import mock_subscription_create, mock_subscription, mock_subscription_list, mock_subscription_update, test_subscription


class TestSubscriptionRepository(BaseMVCTestFactory):
    def test_create(self, real_subscription_repo: SubscriptionRepository, mock_subscription: Subscription):
        data = real_subscription_repo.create(subscription=mock_subscription)

        assert data is not None
        assert data == mock_subscription

    def test_get_all(self, real_subscription_repo: SubscriptionRepository, test_subscription: List[Subscription]):
        data = real_subscription_repo.get_all(skip=0, limit=100)

        assert data is not None
        assert len(data) == len(test_subscription)
        assert data == test_subscription

    def test_get_one(self, real_subscription_repo: SubscriptionRepository, test_subscription: List[Subscription]):
        data = real_subscription_repo.get_one(1)

        assert data is not None
        assert data.id == test_subscription[0].id
        assert data == test_subscription[0]

    def test_update(self, real_subscription_repo: SubscriptionRepository, test_subscription: List[Subscription], mock_subscription: Subscription, mock_subscription_update: Subscription):
        real_subscription_repo.session.add(mock_subscription)
        real_subscription_repo.session.commit()

        original: Subscription = real_subscription_repo.session.get(
            Subscription, mock_subscription.id)

        assert original is not None

        original.status = mock_subscription_update.status
        original.start_date = mock_subscription_update.start_date
        original.end_date = mock_subscription_update.end_date
        original.tenant_id = mock_subscription_update.tenant_id
        original.plan_id = mock_subscription_update.plan_id

        data = real_subscription_repo.update(original)

        assert data is not None

        assert data.status == mock_subscription_update.status
        assert data.start_date.replace(
            tzinfo=timezone.utc) == mock_subscription_update.start_date.replace(tzinfo=timezone.utc)
        assert data.end_date.replace(
            tzinfo=timezone.utc) == mock_subscription_update.end_date.replace(tzinfo=timezone.utc)
        assert data.tenant_id == mock_subscription_update.tenant_id
        assert data.plan_id == mock_subscription_update.plan_id

    def test_delete(self, real_subscription_repo: SubscriptionRepository, test_subscription: List[Subscription], mock_subscription: Subscription):

        real_subscription_repo.session.add(mock_subscription)
        real_subscription_repo.session.commit()

        data = real_subscription_repo.delete(mock_subscription)

        assert data is None
