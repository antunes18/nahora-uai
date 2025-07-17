import pytest
import json
from sqlalchemy.orm import sessionmaker, Session
from fastapi.testclient import TestClient

from api.core.main import app
from api.core.auth import hash_password
from api.core.dependecies import get_user_services

from api.models.dto.user_dto import UserUpdateDTO
from api.models.user import User

from test.mocks.user import mock_user_service, mock_user_repository, mock_user_update
from test.mocks.mock_token_user import auth_header


@pytest.fixture
def test_user(db_session_for_test: Session) -> User:
    """
    Cria um utilizador na base de dados para fins de teste.
    """

    password = hash_password("stringstri")

    user = User(
        username="teste_de_user1",
        email="teste1@teste.com",
        number="1234567891234",
        password=password,
        role="user",
        disabled=False,
    )

    db_session_for_test.add(user)
    db_session_for_test.commit()

    return user


@pytest.fixture
def new_user_json():
    return ({
        "username": "teste_de_user1",
        "email": "teste1@teste.com",
        "number": "1234567891234",
        "password": "stringstri",
        "confirm_password": "stringstri",

    })


@pytest.fixture
def login_user_json():
    return ({
        "email": "teste1@teste.com",
        "password": "stringstri",
    })


class Test_Auth_E2E:

    def test_sign_in(self, client, auth_header, new_user_json):
        response = client.post(
            '/auth/signup', json=new_user_json, headers=auth_header)

        assert response.status_code == 201

        assert response.json()["username"] == "teste_de_user1"
        assert response.json()["email"] == "teste1@teste.com"
        assert response.json()["number"] == int("1234567891234")
        assert response.json()["role"] == "user"
        assert response.json()["disabled"] is False

    def test_login(self, client, auth_header, login_user_json, test_user):
        response = client.post(
            "/auth/signin", json=login_user_json, headers=auth_header)

        assert response.status_code == 200
        assert response.json()["access_token"] is not None
