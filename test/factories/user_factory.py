from api.models.user import User
from api.models.dto.user_dto import UserCreateDTO, UserUpdateDTO
from api.models.enums.roles import Roles
from test.factories.base import BaseTestFactory


class UserFactory(BaseTestFactory):

    @classmethod
    def create(cls, **kwargs) -> User:
        return User(
            username=kwargs.get("username", cls.random_string()),
            email=kwargs.get("email", cls.random_email()),
            phone=kwargs.get("phone", cls.random_phone()),
            password=kwargs.get("password", "stringstri"),
            role=kwargs.get("role", Roles.user),
            disabled=kwargs.get("disabled", False),
            tenant_id=kwargs.get("tenant_id", 1)
        )

    @classmethod
    def dto(cls, **kwargs) -> UserCreateDTO:
        return UserCreateDTO(
            username=kwargs.get("username", cls.random_string()),
            email=kwargs.get("email", cls.random_email()),
            password=kwargs.get("password", "stringstri"),
            confirm_password=kwargs.get("confirm_password", "stringstri"),
            phone=kwargs.get("phone", cls.random_phone()),
            role=kwargs.get("role", Roles.user),
            tenant_id=kwargs.get("tenant_id", 1)
        )

    @classmethod
    def update_dto(cls, **kwargs) -> UserUpdateDTO:
        return UserUpdateDTO(
            username=kwargs.get("username", cls.random_string()),
            phone=kwargs.get("phone", cls.random_phone()),
            password=kwargs.get("password", "nova_senha"),
            confirm_password=kwargs.get("confirm_password", "nova_senha")
        )
