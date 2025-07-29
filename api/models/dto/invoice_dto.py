from pydantic import BaseModel, Field
from datetime import datetime
from api.models.enums.invoice_status import InvoiceStatus


class InvoiceCreateDTO(BaseModel):
    due_time: datetime = Field()
    paid_date: datetime = Field()
    subscription_id: int = Field()

    class Config:
        from_attributes = True


class InvoiceResponseDTO(BaseModel):
    status: InvoiceStatus
    due_time: datetime
    paid_date: datetime
    subscription_id: int

    class Config:
        from_attributes = True


class InvoiceUpdateDTO(BaseModel):
    status: InvoiceStatus
    due_time: datetime
    paid_date: datetime
    subscription_id: int

    class Config:
        from_attributes = True
