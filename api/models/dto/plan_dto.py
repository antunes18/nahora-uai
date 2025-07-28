from pydantic import BaseModel, Field


class PlanCreateDTO(BaseModel):
    name: str = Field()
    price: float = Field(default=0)
    user_limit: int = Field(default=0)
    scheduling_limit: int = Field(default=0)

    class Config:
        from_attributes = True


class PlanResponseDTO(BaseModel):
    name: str = Field()
    price: float = Field()
    user_limit: int = Field(default=0)
    scheduling_limit: int = Field(default=0)

    class Config:
        from_attributes = True


class PlanUpdateDTO(BaseModel):
    name: str = Field()
    price: int = Field(default=0)
    user_limit: int = Field(default=0)
    scheduling_limit: int = Field(default=0)

    class Config:
        from_attributes = True
