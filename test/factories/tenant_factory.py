from test.factories.base import BaseTestFactory

from api.models.tenant import Tenant
from api.models.dto.tenant_dto import TenantCreateDTO, TenantUpdateDTO


class TenantFactory(BaseTestFactory):

    @classmethod
    def create(cls, **kwargs) -> Tenant:
        return Tenant(
            name=kwargs.get("name", cls.random_string()),
            subdomain=kwargs.get("subdomain", cls.random_string()),
            logo_url=kwargs.get("logo_url", cls.random_string()),
            primary_color=kwargs.get("primary_color", cls.random_string())
        )

    @classmethod
    def dto(cls, **kwargs) -> TenantCreateDTO:
        return TenantCreateDTO(
            name=kwargs.get("name", cls.random_string()),
            subdomain=kwargs.get("subdomain", cls.random_string()),
            logo_url=kwargs.get("logo_url", cls.random_string()),
            primary_color=kwargs.get("primary_color", cls.random_string())
        )

    @classmethod
    def update_dto(cls, **kwargs) -> Tenant:
        return Tenant(
            name=kwargs.get("name", cls.random_string()),
            subdomain=kwargs.get("subdomain", cls.random_string()),
            logo_url=kwargs.get("logo_url", cls.random_string()),
            primary_color=kwargs.get("primary_color", cls.random_string())
        )
