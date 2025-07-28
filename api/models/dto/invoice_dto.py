from pydantic import BaseModel, Field
from datetime import datetime


class InvoiceCreateDTO(BaseModel):
    status: str = Field()
    due_time: datetime = Field()
    paid_date: datetime = Field()
    subscription_id: int = Field()

    class Config:
        from_attributes = True


class InvoiceResponseDTO(BaseModel):
    status: str = Field()
    due_time: datetime = Field()
    paid_date: datetime = Field()
    subscription_id: int = Field()

    class Config:
        from_attributes = True


class InvoiceUpdateDTO(BaseModel):
    status: str = Field()
    due_time: datetime = Field()
    paid_date: datetime = Field()
    subscription_id: int = Field()

    class Config:
        from_attributes = True
