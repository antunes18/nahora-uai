import pytest
from sqlalchemy.orm import Session

from api.core.auth import hash_password

from api.models.user import User
from api.models.dto.user_dto import UserCreateDTO, UserLoginDTO, UserUpdateDTO
from api.models.enums.roles import Roles

from test.factories.user_factory import UserFactory


@pytest.fixture(scope="function")
def test_user_create():
    return UserFactory.dto()


@pytest.fixture(scope="function")
def test_user_login():
    return UserLoginDTO(email="email@email.com", password="stringstri")


@pytest.fixture
def mock_user():
    return UserFactory.create()


@pytest.fixture
def mock_user_update():
    return UserFactory.update_dto()


@pytest.fixture
def mock_list_user():
    return UserFactory.create_batch()


@pytest.fixture(scope="function")
def test_user(db_session_for_test: Session) -> User:
    """
    Cria um utilizador na base de dados para fins de teste.
    """

    password = hash_password("stringstri")

    user = User(
        username="teste_de_user1",
        email="teste1@teste.com",
        password="",
        phone="1234567891234",
        role="user",
        disabled=False,
        tenant_id="1"
    )

    user.password = password

    db_session_for_test.add(user)
    db_session_for_test.commit()

    return user


@pytest.fixture
def new_user_json():
    return ({
        "username": "teste_de_user1",
        "email": "teste1@teste.com",
        "phone": "1234567891234",
        "password": "stringstri",
        "confirm_password": "stringstri",
        "tenant_id": "1"

    })


@pytest.fixture
def login_user_json():
    return ({
        "email": "teste1@teste.com",
        "password": "stringstri",
    })
