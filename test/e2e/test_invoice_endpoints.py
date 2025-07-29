from fastapi.testclient import TestClient

from api.core.main import app
from api.core.dependecies import get_invoice_services

from api.models.invoice import Invoice
from api.models.dto.invoice_dto import invoiceUpdateDTO

from test.factories.base import BaseMVCTestFactory

from test.mocks.invoice import mock_invoice_update
from test.mocks.mock_token_user import auth_header

from test.mocks.invoice import mock_invoice, mock_invoice_list, test_invoice, create_invoice_json, update_invoice_json


class Test_invoice_E2E(BaseMVCTestFactory):
    def test_get_all(self, client, test_invoice, auth_header):
        response = client.get("/invoice", headers=auth_header)

        assert response.status_code == 200
        assert len(response.json()) == len(test_invoice)

        app.dependency_overrides.clear()

    def test_get_one(self, client, test_invoice, auth_header):
        response = client.get("/invoice/1", headers=auth_header)

        assert response.status_code == 200
        assert response.json()["status"] == test_invoice[0].status
        assert response.json()["due_date"] == test_invoice[0].due_date
        assert response.json()["paid_date"] == test_invoice[0].paid_date
        assert response.json()[
            "subscription_id"] == test_invoice[0].subscription_id

        app.dependency_overrides.clear()

    def test_create(self, client, test_invoice, auth_header, create_invoice_json):
        response = client.post(
            "/invoice/", headers=auth_header, json=create_invoice_json)

        assert response.status_code == 201
        assert response.json()["status"] == test_invoice[0].status
        assert response.json()[
            "due_date"] == test_invoice[0].due_date.isoformat()
        assert response.json()[
            "paid_date"] == test_invoice[0].paid_date.isoformat()
        assert response.json()[
            "subscription_id"] == test_invoice[0].subscription_id

        app.dependency_overrides.clear()

    def test_update(self, client, test_invoice, update_invoice_json, auth_header):
        response = client.put("/invoice/1",
                              headers=auth_header, json=update_invoice_json)

        assert response.status_code == 204

        result = client.get("/invoice/1", headers=auth_header)

        assert result.status_code == 200
        data = result.json()

        assert data is not None

        assert result.status_code == 200
        assert data["status"] == update_invoice_json["status"]
        assert data["due_date"] == test_invoice[0].due_date
        assert data["paid_date"] == test_invoice[0].paid_date
        assert data["subscription_id"] == update_invoice_json["subscription_id"]

        app.dependency_overrides.clear()

    def test_delete(self, client, test_invoice, auth_header):
        response = client.delete("/invoice/1", headers=auth_header)

        assert response.status_code == 204

        result = client.get("/invoice/1", headers=auth_header)

        assert result.status_code == 404

        app.dependency_overrides.clear()
