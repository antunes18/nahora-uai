from pydantic import BaseModel, Field


class TenantCreateDTO(BaseModel):
    name: str = Field(min_length=3, max_length=250)
    subdomain: str = Field(min_length=3, max_length=250)
    logo_url: str = Field(min_length=3, max_length=250)
    primary_color: str = Field(min_length=3, max_length=250)

    class Config:
        from_attributes = True


class TenantResponseDTO(BaseModel):
    id: int
    name: str
    subdomain: str
    logo_url: str

    class Config:
        from_attributes = True


class TenantUpdateDTO(BaseModel):
    name: str = Field(min_length=3, max_length=250)
    subdomain: str = Field(min_length=3, max_length=250)
    logo_url: str = Field(min_length=3, max_length=250)
    primary_color: str = Field(min_length=3, max_length=250)

    class Config:
        from_attributes = True
