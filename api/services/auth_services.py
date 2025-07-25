from typing import List
from sqlalchemy.orm import Session

from api.core import auth

from api.exceptions.generics import EntityAlreadyExists, EntityNotFound, InvalidData, FieldAlreadyUsed

from api.models.user import User
from api.models.dto.user_dto import UserCreateDTO, UserResponseDTO, UserLoginDTO, UserUpdateDTO

from api.repository.user_repository import UserRepository
from api.repository.tenant_repository import TenantRepository


class UserServices:
    def __init__(self, user_repo: UserRepository, tenant_repo: TenantRepository) -> None:
        self.user_repo = user_repo
        self.tenant_repo = tenant_repo

    def register_user(self, dto: UserCreateDTO):
        if self.user_repo.get_user_by_email(dto.email):
            raise EntityAlreadyExists("Usuário com esse Email")

        if self.user_repo.get_user_by_username(dto.username):
            raise FieldAlreadyUsed("Usuário com esse Username")

        if self.user_repo.get_user_by_phone_number(dto.phone):
            raise FieldAlreadyUsed("Número de Telefone")

        if self.tenant_repo.get_one(dto.tenant_id) and dto.tenant_id != 0:
            raise EntityNotFound("Tenant")

        user = User(
            username=dto.username,
            email=dto.email,
            phone=dto.phone,
            password=auth.hash_password(dto.password),
            disabled=False,
            tenant_id=dto.tenant_id
        )
        return self.user_repo.create_user(user)

    def login(self, user_login: UserLoginDTO) -> auth.Token:
        user_data: UserResponseDTO = self.user_repo.get_user_by_email(
            user_login.email)

        if not user_data:
            raise EntityNotFound("Usuário")

        if auth.verify_password(user_login.password, user_data.password):
            token = auth.sign(user_data)

            return auth.Token(access_token=token)

        raise InvalidData("Email ou Senha de Usuário")

    def get_all(self, skip: int, limit: int):
        return self.user_repo.get_all_users(skip, limit)

    def get_user(self, user_id: int):
        user = self.user_repo.get_user(user_id)

        if not user:
            raise EntityNotFound("User")

        return user

    def get_user_by_email(self, email: str):
        user = self.user_repo.get_user_by_email(email)

        if not user:
            raise EntityNotFound("Usuário")

        return user

    def update_user(self, user_id: int, update_user: UserUpdateDTO):
        user = self.user_repo.get_user(user_id)
        if user is None and user.disabled is True:
            raise EntityNotFound("Usuário")

        if self.user_repo.get_user_by_username(update_user.username) and user.username != update_user.username:
            raise FieldAlreadyUsed("Usuário com esse Username")

        if self.user_repo.get_user_by_phone_number(update_user.phone) and user.phone != update_user.phone:
            raise FieldAlreadyUsed("Número de Telefone")

        return self.user_repo.update_user(user, update_user)

    def delete_user(self, user_id:
                    int):
        user = self.user_repo.get_user(user_id)
        if user is None:
            raise EntityNotFound("Usuário")

        return self.user_repo.disable_user(user)

    def restore_user(self, user_id:
                     int):
        user = self.user_repo.get_user(user_id)
        if user is None:
            raise EntityNotFound("Usuário")

        return self.user_repo.enable_user(user)
