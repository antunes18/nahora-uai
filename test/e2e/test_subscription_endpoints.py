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

from test.mocks.subscription import mock_subscription_list, test_subscription, create_subscription_json, update_subscription_json
from test.mocks.tenant import test_tenant, mock_tenant_list
from test.mocks.plan import test_plan, mock_plan_list


class Test_subscription_E2E(BaseMVCTestFactory):
    def test_get_all(self, client, test_subscription, auth_header):
        response = client.get("/subscription", headers=auth_header)

        assert response.status_code == 200
        assert len(response.json()) == len(test_subscription)

        app.dependency_overrides.clear()

    def test_get_one(self, client, test_subscription, auth_header):
        response = client.get("/subscription/1", headers=auth_header)

        assert response.status_code == 200
        assert response.json()["status"] == test_subscription[0].status
        assert response.json()[
            "start_date"] == test_subscription[0].start_date.isoformat()
        assert response.json()[
            "end_date"] == test_subscription[0].end_date.isoformat()
        assert response.json()["tenant_id"] == test_subscription[0].tenant_id
        assert response.json()["plan_id"] == test_subscription[0].plan_id

        app.dependency_overrides.clear()

    def test_create(self, client, test_subscription, test_tenant, test_plan,  auth_header, create_subscription_json):
        response = client.post(
            "/subscription/", headers=auth_header, json=create_subscription_json)

        assert response.status_code == 201
        assert response.json()["status"] == create_subscription_json["status"]
        assert response.json()["start_date"].startswith(
            create_subscription_json["start_date"].split("+")[0])

        assert response.json()["end_date"].startswith(
            create_subscription_json["end_date"].split("+")[0])

        assert response.json()[
            "tenant_id"] == create_subscription_json["tenant_id"]
        assert response.json()[
            "plan_id"] == create_subscription_json["plan_id"]

        app.dependency_overrides.clear()

    def test_update(self, client, test_subscription, update_subscription_json, test_plan, test_tenant, auth_header):
        response = client.put("/subscription/1",
                              headers=auth_header, json=update_subscription_json)

        assert response.status_code == 204

        result = client.get("/subscription/1", headers=auth_header)

        assert result.json()["status"] == update_subscription_json["status"]
        assert result.json()["start_date"].startswith(
            update_subscription_json["start_date"].split("+")[0])

        assert result.json()["end_date"].startswith(
            update_subscription_json["end_date"].split("+")[0])

        assert result.json()[
            "tenant_id"] == update_subscription_json["tenant_id"]
        assert result.json()[
            "plan_id"] == update_subscription_json["plan_id"]

        app.dependency_overrides.clear()

    def test_delete(self, client, test_subscription, auth_header):
        response = client.delete("/subscription/1", headers=auth_header)

        assert response.status_code == 204

        result = client.get("/subscription/1", headers=auth_header)

        assert result.status_code == 404

        app.dependency_overrides.clear()
