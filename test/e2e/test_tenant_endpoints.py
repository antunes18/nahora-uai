from fastapi.testclient import TestClient

from api.core.main import app
from api.core.dependecies import get_tenant_services

from api.models.tenant import Tenant
from api.models.dto.tenant_dto import TenantUpdateDTO

from test.factories.base import BaseMVCTestFactory

from test.mocks.tenant import mock_tenant_update
from test.mocks.mock_token_user import auth_header

from test.mocks.tenant import mock_tenant, mock_tenant_list, test_tenant, create_tenant_json, update_tenant_json
from test.mocks.user import test_user
from test.mocks.scheduling import test_scheduling, mock_scheduling_list


class Test_Tenant_E2E(BaseMVCTestFactory):
    def test_get_all(self, client, test_tenant, auth_header):
        response = client.get("/tenant", headers=auth_header)

        assert response.status_code == 200
        assert len(response.json()) == len(test_tenant)

        app.dependency_overrides.clear()

    def test_get_one(self, client, test_tenant, auth_header):
        response = client.get("/tenant/1", headers=auth_header)

        assert response.status_code == 200
        assert response.json()["name"] == test_tenant[0].name
        assert response.json()["subdomain"] == test_tenant[0].subdomain
        assert response.json()["logo_url"] == test_tenant[0].logo_url

        app.dependency_overrides.clear()

    def test_create(self, client, test_tenant, auth_header, create_tenant_json):
        response = client.post(
            "/tenant/", headers=auth_header, json=create_tenant_json)

        assert response.status_code == 201
        assert response.json()["name"] == create_tenant_json["name"]
        assert response.json()["subdomain"] == create_tenant_json["subdomain"]
        assert response.json()["logo_url"] == create_tenant_json["logo_url"]

        app.dependency_overrides.clear()

    def test_update(self, client, test_tenant, update_tenant_json, auth_header):
        response = client.put("/tenant/1",
                              headers=auth_header, json=update_tenant_json)

        assert response.status_code == 204

        result = client.get("/tenant/1", headers=auth_header)

        assert result.status_code == 200
        data = result.json()

        assert data is not None

        assert data["id"] == 1
        assert data["name"] == update_tenant_json["name"]
        assert data["subdomain"] == update_tenant_json["subdomain"]
        assert data["logo_url"] == update_tenant_json["logo_url"]

        app.dependency_overrides.clear()

    def test_delete(self, client, test_tenant, auth_header):
        response = client.delete("/tenant/1", headers=auth_header)

        assert response.status_code == 204

        result = client.get("/tenant/1", headers=auth_header)

        assert result.status_code == 404

        app.dependency_overrides.clear()

    def test_get_users(self, client, test_tenant, test_user, auth_header):
        response = client.get("/tenant/1/users", headers=auth_header)

        assert response.status_code == 200

        assert len(response.json()) == len(
            [user for user in test_user if user.tenant_id == 1])

        app.dependency_overrides.clear()

    def test_get_schedulings(self, client, test_tenant, test_scheduling, auth_header):
        response = client.get("/tenant/1/schedulings", headers=auth_header)

        assert response.status_code == 200

        assert len(response.json()) == len(
            [scheduling for scheduling in test_scheduling if scheduling.tenant_id == 1])

        app.dependency_overrides.clear()
