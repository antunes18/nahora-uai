from datetime import datetime, timedelta, timezone
from test.factories.base import BaseTestFactory

from api.models.subscription import Subscription
from api.models.dto.subscription_dto import SubscriptionCreateDTO, SubscriptionResponseDTO, SubscriptionUpdateDTO
from api.models.enums.subscription_status import SubscriptionStatus


class SubscriptionTestFactory(BaseTestFactory):

    @classmethod
    def create(cls, **kwargs) -> Subscription:
        return Subscription(
            status=kwargs.get("status",  cls.random_enum(SubscriptionStatus)),
            start_date=kwargs.get("start_date", datetime.now(
                timezone.utc) + timedelta(days=1)),
            end_date=kwargs.get("end_date", datetime.now(
                timezone.utc) + timedelta(days=2)),
            tenant_id=kwargs.get("tenant_id", 1),
            plan_id=kwargs.get("plan_id", 1)
        )

    @classmethod
    def dto(cls, **kwargs):
        return SubscriptionCreateDTO(
            status=kwargs.get("status", cls.random_enum(SubscriptionStatus)),
            start_date=kwargs.get("start_date", datetime.now(
                timezone.utc) + timedelta(days=1)),
            end_date=kwargs.get("end_date", datetime.now(
                timezone.utc) + timedelta(days=2)),
            tenant_id=kwargs.get("tenant_id", 1),
            plan_id=kwargs.get("plan_id", 1)
        )

    @classmethod
    def update_dto(cls, **kwargs):
        return SubscriptionUpdateDTO(
            status=kwargs.get("status", cls.random_enum(SubscriptionStatus)),
            start_date=kwargs.get("start_date", datetime.now(
                timezone.utc) + timedelta(days=1)),
            end_date=kwargs.get("end_date", datetime.now(
                timezone.utc) + timedelta(days=2)),
            tenant_id=kwargs.get("tenant_id", 1),
            plan_id=kwargs.get("plan_id", 1)
        )

    @classmethod
    def create_json(cls, **kwargs):
        return {{
            "status": kwargs.get("status", cls.random_enum(SubscriptionStatus)),
            "start_date": kwargs.get("start_date", datetime.now(timezone.utc) + timedelta(days=1)),
            "end_date": kwargs.get("end_date", datetime.now(timezone.utc) + timedelta(days=2)),
            "tenant_id": kwargs.get("tenant_id", 1),
            "plan_id": kwargs.get("plan_id", 1)
        }}

    @classmethod
    def update_json(cls, **kwargs):
        return {{
            "status": kwargs.get("status", cls.random_enum(SubscriptionStatus)),
            "start_date": kwargs.get("start_date", datetime.now(timezone.utc) + timedelta(days=1)),
            "end_date": kwargs.get("end_date", datetime.now(timezone.utc) + timedelta(days=2)),
            "tenant_id": kwargs.get("tenant_id", 1),
            "plan_id": kwargs.get("plan_id", 1)
        }}
