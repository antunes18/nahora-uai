from typing import List
from unittest.mock import Mock

from api.models.dto.subscription_dto import SubscriptionResponseDTO, SubscriptionUpdateDTO
from api.models.subscription import Subscription
from api.models.tenant import Tenant
from api.models.plan import Plan

from api.services.subscription_services import SubscriptionService

from test.factories.base import BaseMVCTestFactory

from test.dependencies import (
    mock_subscription_services,
    mock_subscription_repo,
    mock_tenant_repo,
    mock_plan_repo
)

from test.mocks.subscription import (
    mock_subscription,
    mock_subscription_create,
    mock_subscription_list,
    mock_subscription_update,
)

from test.mocks.tenant import mock_tenant
from test.mocks.plan import mock_plan


class TestsubscriptionServices(BaseMVCTestFactory):

    def test_get_all(self, mock_subscription_list: List[SubscriptionResponseDTO], mock_subscription_services: SubscriptionService, mock_subscription_repo: Mock):
        mock_subscription_repo.get_all.return_value = mock_subscription_list
        response = mock_subscription_services.get_all(skip=0, limit=100)

        assert response is not None
        assert len(response) == len(mock_subscription_list)

    def test_get_one(self, mock_subscription: Subscription, mock_subscription_services: SubscriptionService, mock_subscription_repo: Mock):
        mock_subscription_repo.get_one.return_value = mock_subscription

        response: Subscription = mock_subscription_services.get_one(1)

        assert response is not None
        assert response == mock_subscription

    def test_create(self, mock_subscription: Subscription, mock_plan: Plan, mock_tenant: Tenant, mock_subscription_services: SubscriptionService, mock_subscription_repo: Mock, mock_plan_repo: Mock, mock_tenant_repo: Mock):
        mock_tenant_repo.get_one.return_value = mock_tenant
        mock_plan_repo.get_one.return_value = mock_plan

        mock_subscription_repo.create.return_value = mock_subscription

        response = mock_subscription_services.create(mock_subscription)

        assert response is not None
        assert response == mock_subscription

    def test_update(self, mock_subscription: Subscription, mock_subscription_update: SubscriptionUpdateDTO,  mock_subscription_services: SubscriptionService, mock_subscription_repo: Mock, mock_tenant_repo: Mock, mock_plan_repo: Mock):
        mock_tenant_repo.get_one.return_value = mock_tenant
        mock_plan_repo.get_one.return_value = mock_plan

        mock_subscription_repo.get_one.return_value = mock_subscription
        mock_subscription_repo.update.return_value = (
            mock_subscription_update
        )

        response = mock_subscription_services.update(
            mock_subscription.id, mock_subscription_update
        )

        assert response is not None
        assert response == mock_subscription_update

    def test_delete(self, mock_subscription: Subscription, mock_subscription_update: SubscriptionUpdateDTO,  mock_subscription_services: SubscriptionService, mock_subscription_repo: Mock):
        mock_subscription_repo.get_one.return_value = mock_subscription
        mock_subscription_repo.delete.return_value = None

        response = mock_subscription_services.delete(mock_subscription.id)

        assert response is None
