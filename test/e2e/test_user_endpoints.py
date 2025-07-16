import pytest
import json
from sqlalchemy.orm import sessionmaker, Session
from fastapi.testclient import TestClient

from api.core.main import app
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
    users = [
        User(
            username="teste_de_user1",
            email="teste1@teste.com",
            number="1234567891234",
            password="stringstri",
            role="user",
            disabled=False,
        ),
        User(
            username="teste_de_user2",
            email="teste2@teste.com",
            number="9876543210111",
            password="stringstri",
            role="user",
            disabled=False,
        ),
    ]

    for user in users:
        db_session_for_test.add(user)
        db_session_for_test.commit()

    return users


@pytest.fixture
def user_update_json():
    return ({
        "username":         "update_user",
        "number":           "1234567891234",
        "password":         "stringupdate",
        "confirm_password": "stringupdate",

    })


class Test_User_Endpoint:
    def test_get_all_users(self, client, test_user, auth_header):
        """
        Tests the GET /user/ endpoint to retrieve all users.
        """
        # Override the dependency for this test
        # This ensures that when get_user_services is called by the FastAPI app,
        # it returns our mock_user_services instead of the real one.

        response = client.get("/user/", headers=auth_header)

        # Assertions
        assert response.status_code == 200
        assert len(response.json()) == 2

        assert response.json()[0]["id"] == 1
        assert response.json()[1]["email"] == "teste2@teste.com"

        app.dependency_overrides.clear()

    def test_user_get(self, client, test_user, auth_header):
        """
        Tests the GET /user/{id} endpoint to retrieve user.
        """
        # Override the dependency for this test
        # This ensures that when get_user_services is called by the FastAPI app,
        # it returns our mock_user_services instead of the real one.

        response = client.get("/user/1", headers=auth_header)

        # Assertions
        assert response.status_code == 200

        assert response.json()["id"] == 1
        assert response.json()["email"] == "teste1@teste.com"

        app.dependency_overrides.clear()

    def test_user_update_e2e(self, client, test_user, auth_header, user_update_json):

        response = client.put(
            "/user/1", headers=auth_header, json=user_update_json
        )
        assert response.status_code == 200
        assert response.json() is not None

        assert response.json()["email"] == "teste1@teste.com"
        assert response.json()["username"] == "update_user"
        assert response.json()["number"] == "1234567891233"

        app.dependency_overrides.clear()
