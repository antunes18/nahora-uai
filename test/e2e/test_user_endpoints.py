import pytest
import json
from sqlalchemy.orm import sessionmaker, Session
from fastapi.testclient import TestClient

from api.core.main import app
from api.core.dependecies import get_user_services

from api.models.dto.user_dto import UserUpdateDTO
from api.models.user import User

from test.mocks.user import mock_user_update, test_user, user_update_json
from test.mocks.mock_token_user import auth_header


class Test_User_E2E:
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
        assert len(response.json()) == len(test_user)

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
        assert response.status_code == 204

        result = client.get(
            "user/1", headers=auth_header
        )

        assert result.json() is not None

        assert result.json()["email"] == "teste1@teste.com"
        assert result.json()["username"] == "update_user"
        assert result.json()["phone"] == "1234567891234"

        app.dependency_overrides.clear()

    def test_user_delete_e2e(self, client, test_user, auth_header):
        response = client.delete("/user/1", headers=auth_header)

        assert response.status_code == 204
        app.dependency_overrides.clear()
