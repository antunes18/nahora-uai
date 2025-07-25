from fastapi.testclient import TestClient

from api.core.main import app
from api.core.dependecies import get_tenant_services

from api.models.tenant import Tenant
from api.models.dto.tenant_dto import TenantUpdateDTO

from test.mocks.tenant import mock_tenant_update
from test.mocks.mock_token_user import auth_header

from test.mocks.tenant import mock_tenant, mock_tenant_list, test_tenant, create_tenant_json, update_tenant_json


class Test_Tenant_E2E:
    def test_get_all_tenant(self, client, test_tenant, auth_header):
        response = client.get("/tenant", headers=auth_header)

        assert response.status_code == 200
        assert len(response.json()) == len(test_tenant)

        app.dependency_overrides.clear()

    def test_get_one_tenant(self, client, test_tenant, auth_header):
        response = client.get("/tenant/1", headers=auth_header)

        assert response.status_code == 200
        assert response.json()["name"] == test_tenant[0].name
        assert response.json()["subdomain"] == test_tenant[0].subdomain
        assert response.json()["logo_url"] == test_tenant[0].logo_url

        app.dependency_overrides.clear()

    # def test_create_tenant(self, client, test_tenant, auth_header, create_tenant_json):
    #     response = client.post(
    #         "/tenant/", headers=auth_header, json=create_tenant_json)
    #
    #     assert response.status_code == 201
    #     assert response.json()["name"] == create_tenant_json.name
    #     assert response.json()["subdomain"] == create_tenant_json.subdomain
    #     assert response.json()["logo_url"] == create_tenant_json.logo_url
    #     assert response.json()[
    #         "primary_color"] == create_tenant_json.primary_color
    #
    #     app.dependency_overrides.clear()
    #
    # def test_update_tenant(self, client, test_tenant, update_tenant_json, auth_header):
    #     response = client.put("/tenant/update/1",
    #                           headers=auth_header, json=update_tenant_json)
    #
    #     assert response.status_code == 204
    #
    #     result = client.get("/tenant/1", headers=auth_header)
    #     assert result.json()["name"] == update_tenant_json.name
    #     assert result.json()["subdomain"] == update_tenant_json.subdomain
    #     assert result.json()["logo_url"] == update_tenant_json.logo_url
    #     assert result.json()[
    #         "primary_color"] == update_tenant_json.primary_color
    #
    #     app.dependency_overrides.clear()
    #
    # def test_delete_tenant(self, client, test_tenant, auth_header):
    #     response = client.delete("/tenant/1", headers=auth_header)
    #
    #     assert response.status_code == 204
    #
    #     result = client.get("/tenant/1", headers=auth_header)
    #
    #     assert result.status_code == 404
    #
    #     app.dependency_overrides.clear()
