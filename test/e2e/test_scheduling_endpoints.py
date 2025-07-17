import pytest
import datetime
import json
from sqlalchemy.orm import sessionmaker, Session
from fastapi.testclient import TestClient

from api.core.main import app
from api.core.dependecies import get_user_services

from api.models.dto.user_dto import UserUpdateDTO
from api.models.user import User

from test.mocks.user import mock_user_service, mock_user_repository, mock_user_update
from test.mocks.mock_token_user import auth_header

from test.mocks.scheduling import mock_scheduling_list
from test.mocks.user import mock_user


@pytest.fixture()
def test_scheduling(db_session_for_test: Session, mock_scheduling_list, mock_user):
    """
    Cria um utilizador na base de dados para fins de teste.
    """

    for scheduling in mock_scheduling_list:
        db_session_for_test.add(scheduling)
        db_session_for_test.commit()

    return mock_scheduling_list


@pytest.fixture
def create_scheduling():
    return ({
        "date": "2030-07-16T23:15:36.736Z",
        "hour": 16,
        "name": "client_username",
        "user_id": 1,
        "phone": "1234567891231"

    })


@pytest.fixture
def update_scheduling():
    return ({
        "date": "2030-07-16T23:15:36.736Z",
        "hour": 18,
        "name": "update_client_username",
        "user_id": 1,
        "phone": "1234567891231"

    })


class Test_Scheduling_E2E:
    def test_get_all_scheduling(self, client, test_scheduling, auth_header):
        response = client.get("/scheduling", headers=auth_header)

        assert response.status_code == 200
        assert len(response.json()) == 4

        app.dependency_overrides.clear()

    def test_get_one_scheduling(self, client, test_scheduling, auth_header):
        response = client.get("/scheduling/1", headers=auth_header)

        assert response.status_code == 200
        assert response.json()["hour"] == 12
        assert response.json()["date"] == "2030-06-16T00:00:00"
        assert response.json()["name"] == "test1"
        assert response.json()["phone"] == str(1234567891231)

        app.dependency_overrides.clear()

    def test_create_scheduling(self, client, test_scheduling, auth_header, create_scheduling):
        response = client.post(
            "/scheduling/", headers=auth_header, json=create_scheduling)

        assert response.status_code == 201
        assert response.json()["hour"] == 16
        assert response.json()["date"] == "2030-07-16T23:15:36.736000"
        assert response.json()["name"] == "client_username"
        assert response.json()["phone"] == str(1234567891231)

        app.dependency_overrides.clear()

    def test_update_scheduling(self, client, test_scheduling, update_scheduling, auth_header):
        response = client.put("/scheduling/update/1",
                              headers=auth_header, json=update_scheduling)

        assert response.status_code == 204

        result = client.get("/scheduling/1", headers=auth_header)
        assert result.json()["hour"] == 18
        assert result.json()["date"] == "2030-07-16T23:15:36.736000"
        assert result.json()["name"] == "update_client_username"
        assert result.json()["phone"] == str(1234567891231)

        app.dependency_overrides.clear()

    def test_delete_scheduling(self, client, test_scheduling, auth_header):
        response = client.delete("/scheduling/delete/1", headers=auth_header)

        assert response.status_code == 204

        result = client.get("/scheduling/1", headers=auth_header)

        assert result.status_code == 404

        app.dependency_overrides.clear()

    def test_restore_scheduling(self, client, test_scheduling, auth_header):

        client.delete("/scheduling/delete/1", headers=auth_header)
        response = client.put("/scheduling/restore/1", headers=auth_header)

        assert response.status_code == 204

        result = client.get("/scheduling/1", headers=auth_header)

        assert result.status_code == 200

        app.dependency_overrides.clear()
