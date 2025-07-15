from pydantic import BaseModel, ConfigDict
from pydantic import BaseModel

from datetime import datetime


class SchedulingDTO(BaseModel):
    id: int
    date: datetime
    hour: int
    name: str
    user_id: int
    phone: str


class SchedulingCreateDto(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    date: datetime
    hour: int
    name: str
    user_id: int
    phone: str
