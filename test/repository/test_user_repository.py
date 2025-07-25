from api.models.dto.user_dto import UserCreateDTO, UserUpdateDTO
from api.repository.user_repository import UserRepository
from api.models.user import User

from test.dependencies import (
    real_user_repo
)

from test.mocks.user import (
    mock_user,
    mock_list_user,
    mock_user_update,
)


class TestUserRepository:
    def test_create_user(
        self, real_user_repo: UserRepository, mock_user: User
    ):
        data = real_user_repo.create_user(mock_user)

        assert data is not None
        assert data.email == mock_user.email
        assert data.username == mock_user.username
        assert data.phone == mock_user.phone
        assert data.role == mock_user.role
        assert data.disabled == mock_user.disabled

    def test_get_all_user(
        self, real_user_repo: UserRepository, mock_list_user: list[User]
    ):
        real_user_repo.session.add_all(mock_list_user)
        real_user_repo.session.commit()

        data = real_user_repo.get_all_users(skip=0, limit=100)

        assert data is not None
        assert len(data) == len(mock_list_user)

        email = [x.email for x in data]
        assert mock_list_user[0].email in email
        assert mock_list_user[1].email in email

    def test_get_user(self, real_user_repo: UserRepository, mock_user: User):
        real_user_repo.session.add(mock_user)
        real_user_repo.session.commit()

        data = real_user_repo.get_user(user_id=1)
        assert data is not None

    def test_get_user_by_email(
        self, real_user_repo: UserRepository, mock_user: User
    ):
        real_user_repo.session.add(mock_user)
        real_user_repo.session.commit()

        data = real_user_repo.get_user_by_email(mock_user.email)

        assert data is not None
        assert data.email == mock_user.email
        assert data.username == mock_user.username
        assert data.phone == mock_user.phone
        assert data.role == mock_user.role
        assert data.disabled == mock_user.disabled

    def test_get_user_by_username(
        self, real_user_repo: UserRepository, mock_user: User
    ):
        real_user_repo.session.add(mock_user)
        real_user_repo.session.commit()

        data = real_user_repo.get_user_by_username(mock_user.username)

        assert data is not None
        assert data.email == mock_user.email
        assert data.username == mock_user.username
        assert data.phone == mock_user.phone
        assert data.role == mock_user.role
        assert data.disabled == mock_user.disabled

    def test_get_user_by_phone_number(
        self, real_user_repo: UserRepository, mock_user
    ):
        real_user_repo.session.add(mock_user)
        real_user_repo.session.commit()

        data = real_user_repo.get_user_by_phone_number(mock_user.phone)

        assert data is not None
        assert data.email == mock_user.email
        assert data.username == mock_user.username
        assert data.phone == mock_user.phone
        assert data.role == mock_user.role
        assert data.disabled == mock_user.disabled

    def test_update_user(
        self,
        real_user_repo: UserRepository,
        mock_user: UserCreateDTO,
        mock_user_update: UserUpdateDTO,
    ):
        real_user_repo.session.add(mock_user)
        real_user_repo.session.commit()

        data = real_user_repo.update_user(mock_user, mock_user_update)

        assert data is not None
        assert data.username == mock_user_update.username
        assert data.phone == mock_user_update.phone

    def test_delete_user(self, real_user_repo: UserRepository, mock_user: User):
        real_user_repo.session.add(mock_user)
        real_user_repo.session.commit()

        data = real_user_repo.disable_user(mock_user)

        assert data is not None
        assert data.disabled is True

    def test_restore_user(self, real_user_repo: UserRepository, mock_user: User):
        real_user_repo.session.add(mock_user)
        real_user_repo.session.commit()

        data = real_user_repo.enable_user(mock_user)

        assert data is not None
        assert data.disabled is False
