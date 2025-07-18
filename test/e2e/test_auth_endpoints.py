import pytest
import json
from sqlalchemy.orm import sessionmaker, Session
from fastapi.testclient import TestClient

from api.core.main import app
from api.core.dependecies import get_user_services

from api.models.dto.user_dto import UserUpdateDTO
from api.models.user import User

from test.mocks.user import mock_user_service, mock_user_repository, mock_user_update, new_user_json, login_user_json, test_user
from test.mocks.mock_token_user import auth_header


class Test_Auth_E2E:

    def test_sign_in(self, client, auth_header, new_user_json):
        response = client.post(
            '/auth/signup', json=new_user_json, headers=auth_header)

        assert response.status_code == 201

        assert response.json()["username"] == "teste_de_user1"
        assert response.json()["email"] == "teste1@teste.com"
        assert response.json()["phone"] == "1234567891234"
        assert response.json()["role"] == "user"
        assert response.json()["disabled"] is False

    def test_login(self, client, auth_header, login_user_json, test_user):
        response = client.post(
            "/auth/signin", json=login_user_json, headers=auth_header)

        assert response.status_code == 200
        assert response.json()["access_token"] is not None
