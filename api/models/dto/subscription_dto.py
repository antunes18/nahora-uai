from pydantic import BaseModel, Field
from datetime import datetime


class SubscriptionCreateDTO(BaseModel):
    status: str = Field()
    start_date: datetime = Field()
    end_date: datetime = Field()

    tenant_id: int = Field()
    plan_id: int = Field()

    class Config:
        from_attributes = True


class SubscriptionResponseDTO(BaseModel):
    status: str = Field()
    start_date: datetime = Field()
    end_date: datetime = Field()

    tenant_id: int = Field()
    plan_id: int = Field()

    class Config:
        from_attributes = True


class SubscriptionUpdateDTO(BaseModel):
    status: str = Field()
    start_date: datetime = Field()
    end_date: datetime = Field()

    tenant_id: int = Field()
    plan_id: int = Field()

    class Config:
        from_attributes = True
