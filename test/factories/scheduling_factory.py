import random
from datetime import datetime, timedelta, timezone

from api.models.scheduling import Scheduling
from api.models.dto.scheduling_dto import SchedulingCreateDto, SchedulingUpdateDTO

from test.factories.base import BaseTestFactory
from test.factories.user_factory import UserFactory


class SchedulingFactory(BaseTestFactory):

    @classmethod
    def create(cls, **kwargs) -> Scheduling:
        return Scheduling(
            tenant_id=kwargs.get("tenant_id", 1),
            hour=kwargs.get("hour", random.randint(14, 18)),
            date=kwargs.get("date", datetime.now(
                timezone.utc) + timedelta(days=1)),
            name=kwargs.get("name", "Client Test"),
            phone=kwargs.get("phone", cls.random_phone()),
            user_id=kwargs.get("user_id", 1),
            user=kwargs.get("user", UserFactory.create()),
            is_deleted=kwargs.get("is_deleted", False)

        )

    @classmethod
    def dto(cls, **kwargs) -> SchedulingCreateDto:
        return SchedulingCreateDto(
            tenant_id=kwargs.get("tenant_id", 1),
            hour=kwargs.get("hour", random.randint(14, 18)),
            date=kwargs.get("date", datetime.now(
                timezone.utc) + timedelta(days=1)),
            name=kwargs.get("name", cls.random_string()),
            phone=kwargs.get("phone", cls.random_phone()),
            user_id=kwargs.get("user_id", 1),
        )

    @classmethod
    def update_dto(cls, **kwargs) -> Scheduling:
        return Scheduling(
            tenant_id=kwargs.get("tenant_id", 1),
            hour=kwargs.get("hour", random.randint(14, 18)),
            date=kwargs.get("date", datetime.now(
                timezone.utc) + timedelta(days=1)),
            name=kwargs.get("name", "Client Test"),
            phone=kwargs.get("phone", cls.random_phone()),
            user_id=kwargs.get("user_id", 1),
            user=kwargs.get("user", UserFactory.create()),
            is_deleted=kwargs.get("is_deleted", False)

        )
