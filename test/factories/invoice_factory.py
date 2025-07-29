from datetime import datetime, timezone, timedelta

from test.factories.base import BaseTestFactory

from api.models.invoice import Invoice
from api.models.dto.invoice_dto import InvoiceCreateDTO, InvoiceUpdateDTO
from api.models.enums.invoice_status import InvoiceStatus


class InvoiceFactory(BaseTestFactory):

    @classmethod
    def create(cls, **kwargs) -> Invoice:
        return Invoice(
            status=kwargs.get("status", cls.random_enum(InvoiceStatus)),
            due_time=kwargs.get("due_time", (datetime.now(
                timezone.utc) + timedelta(days=1))),
            paid_date=kwargs.get("paid_date", (datetime.now(
                timezone.utc) + timedelta(days=3))),
            subscription_id=kwargs.get("subscription_id", 1)
        )

    @classmethod
    def dto(cls, **kwargs) -> InvoiceCreateDTO:
        return InvoiceCreateDTO(
            due_time=kwargs.get("due_time", (datetime.now(
                timezone.utc) + timedelta(days=1))),
            paid_date=kwargs.get("paid_date", (datetime.now(
                timezone.utc) + timedelta(days=3))),
            subscription_id=kwargs.get("subscription_id", 1)
        )

    @classmethod
    def update_dto(cls, **kwargs) -> InvoiceUpdateDTO:
        return InvoiceUpdateDTO(
            status=kwargs.get("status", cls.random_enum(InvoiceStatus)),
            due_time=kwargs.get("due_time", (datetime.now(
                timezone.utc) + timedelta(days=1))),
            paid_date=kwargs.get("paid_date", (datetime.now(
                timezone.utc) + timedelta(days=3))),
            subscription_id=kwargs.get("subscription_id", 1)
        )

    @classmethod
    def create_json(cls, **kwargs):
        return ({
            "due_time": kwargs.get("due_time", (datetime.now(
                timezone.utc) + timedelta(days=1)).isoformat()),
            "paid_date": kwargs.get("paid_date", (datetime.now(
                timezone.utc) + timedelta(days=3)).isoformat()),
            "subscription_id": kwargs.get("subscription_id", 1)
        })

    @classmethod
    def update_json(cls, **kwargs):
        return ({
            "status": kwargs.get("status", cls.random_enum(InvoiceStatus)),
            "due_time": kwargs.get("due_time", (datetime.now(
                timezone.utc) + timedelta(days=1)).isoformat()),
            "paid_date": kwargs.get("paid_date", (datetime.now(
                timezone.utc) + timedelta(days=3)).isoformat()),
            "subscription_id": kwargs.get("subscription_id", 1)
        })
