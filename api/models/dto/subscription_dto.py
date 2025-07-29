from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from api.models.enums.subscription_status import SubscriptionStatus


class SubscriptionCreateDTO(BaseModel):
    status: SubscriptionStatus = SubscriptionStatus.active
    start_date: datetime = Field()
    end_date: datetime = Field()

    tenant_id: int = Field()
    plan_id: int = Field()

    model_config = ConfigDict(from_attributes=True)


class SubscriptionResponseDTO(BaseModel):
    status: SubscriptionStatus
    start_date: datetime
    end_date: datetime

    tenant_id: int
    plan_id: int

    model_config = ConfigDict(from_attributes=True)


class SubscriptionUpdateDTO(BaseModel):
    status: SubscriptionStatus
    start_date: datetime = Field()
    end_date: datetime = Field()

    tenant_id: int = Field()
    plan_id: int = Field()

    model_config = ConfigDict(from_attributes=True)
