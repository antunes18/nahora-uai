from test.factories.base import BaseTestFactory

from api.models.plan import Plan
from api.models.dto.plan_dto import PlanCreateDTO, PlanUpdateDTO


class PlanTestFactory(BaseTestFactory):

    @classmethod
    def create(cls, **kwargs) -> Plan:
        return Plan(
            name=kwargs.get("name", cls.random_string()),
            price=kwargs.get("price", cls.random_number()),
            user_limit=kwargs.get("user_limit", cls.random_number(1, 10)),
            scheduling_limit=kwargs.get(
                "scheduling_limit", cls.random_number(1, 100))

        )

    def dto(cls, **kwargs) -> PlanCreateDTO:
        return PlanCreateDTO(
            name=kwargs.get("name", cls.random_string()),
            price=kwargs.get("price", cls.random_number()),
            user_limit=kwargs.get("user_limit", cls.random_number(1, 10)),
            scheduling_limit=kwargs.get(
                "scheduling_limit", cls.random_number(1, 100))

        )

    def update_dto(cls, **kwargs) -> PlanUpdateDTO:
        return PlanUpdateDTO(
            name=kwargs.get("name", cls.random_string()),
            price=kwargs.get("price", cls.random_number()),
            user_limit=kwargs.get("user_limit", cls.random_number(1, 10)),
            scheduling_limit=kwargs.get(
                "scheduling_limit", cls.random_number(1, 100))

        )

    def create_json(cls, **kwargs):
        return ({
            "name": kwargs.get("name", cls.random_string()),
            "price": kwargs.get("price", cls.random_number()),
            "user_limit": kwargs.get("user_limit", cls.random_number(1, 10)),
            "scheduling_limit": kwargs.get("scheduling_limit", cls.random_number(1, 100)),
        })

    def update_json(cls, **kwargs):
        return ({
            "name": kwargs.get("name", cls.random_string()),
            "price": kwargs.get("price", cls.random_number()),
            "user_limit": kwargs.get("user_limit", cls.random_number(1, 10)),
            "scheduling_limit": kwargs.get("scheduling_limit", cls.random_number(1, 100)),
        })
