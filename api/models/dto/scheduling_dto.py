from pydantic import BaseModel

from datetime import datetime


class SchedulingDTO(BaseModel):
    date: datetime
    hour: int
    name: str
    user_id: int
    phone: str


class SchedulingCreateDto(BaseModel):
    date: datetime
    hour: int
    name: str
    user_id: int
    phone: str

    class Config:
        from_attributes = True
