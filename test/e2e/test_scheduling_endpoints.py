import pytest
from datetime import datetime, timezone

from sqlalchemy.orm import sessionmaker, Session
from fastapi.testclient import TestClient

from api.core.main import app
from api.core.dependecies import get_user_services

from api.models.dto.user_dto import UserUpdateDTO
from api.models.user import User

from test.factories.base import BaseMVCTestFactory

from test.mocks.user import mock_user_update
from test.mocks.mock_token_user import auth_header

from test.mocks.scheduling import mock_scheduling_list, test_scheduling, create_scheduling_json, update_scheduling_json
from test.mocks.user import mock_user
from test.mocks.tenant import test_tenant, mock_tenant_list


class Test_Scheduling_E2E(BaseMVCTestFactory):
    def test_get_all(self, client, test_scheduling, auth_header):
        response = client.get("/scheduling", headers=auth_header)

        assert response.status_code == 200
        assert len(response.json()) == len(test_scheduling)

        app.dependency_overrides.clear()

    def test_get_all_scheduling_by_user(self, client, test_scheduling, auth_header):
        response = client.get("/scheduling/user/1", headers=auth_header)

        assert response.status_code == 200
        assert len(response.json()) == len(
            [scheduling for scheduling in test_scheduling if scheduling.id == 1])

        app.dependency_overrides.clear()

    def test_get_one(self, client, test_scheduling, auth_header):
        response = client.get("/scheduling/1", headers=auth_header)

        assert response.status_code == 200
        assert response.json()["hour"] == test_scheduling[0].hour
        assert response.json()["date"] == test_scheduling[0].date.isoformat()
        assert response.json()["name"] == test_scheduling[0].name
        assert response.json()["phone"] == test_scheduling[0].phone

        app.dependency_overrides.clear()

    def test_create(self, client, test_scheduling, test_tenant,  auth_header, create_scheduling_json):
        response = client.post(
            "/scheduling/", headers=auth_header, json=create_scheduling_json)

        assert response.status_code == 201
        assert response.json()["hour"] == create_scheduling_json["hour"]
        assert response.json()["date"].startswith(
            create_scheduling_json["date"].split("+")[0])

        assert response.json()["name"] == create_scheduling_json["name"]
        assert response.json()["phone"] == create_scheduling_json["phone"]

        app.dependency_overrides.clear()

    def test_update(self, client, test_scheduling, update_scheduling_json, auth_header):
        response = client.put("/scheduling/update/1",
                              headers=auth_header, json=update_scheduling_json)

        assert response.status_code == 204

        result = client.get("/scheduling/1", headers=auth_header)
        assert result.json()["hour"] == update_scheduling_json["hour"]
        assert result.json()["date"].startswith(
            update_scheduling_json["date"].split("+")[0])

        assert result.json()["name"] == update_scheduling_json["name"]
        assert result.json()["phone"] == update_scheduling_json["phone"]

        app.dependency_overrides.clear()

    def test_delete(self, client, test_scheduling, auth_header):
        response = client.delete("/scheduling/delete/1", headers=auth_header)

        assert response.status_code == 204

        result = client.get("/scheduling/1", headers=auth_header)

        assert result.status_code == 404

        app.dependency_overrides.clear()

    def test_restore(self, client, test_scheduling, auth_header):

        client.delete("/scheduling/delete/1", headers=auth_header)
        response = client.put("/scheduling/restore/1", headers=auth_header)

        assert response.status_code == 204

        result = client.get("/scheduling/1", headers=auth_header)

        assert result.status_code == 200

        app.dependency_overrides.clear()
