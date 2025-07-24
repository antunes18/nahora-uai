from typing import List

from sqlalchemy.orm import Session
from api.models.tenant import Tenant


class TenantRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create_tenant(self, tenant: Tenant) -> Tenant:
        self.session.add(tenant)
        self.session.commit()
        self.session.refresh(tenant)

        return tenant

    def get_all(self, skip: int, limit: int) -> List[Tenant]:
        return self.session.query(Tenant).offset(skip).limit(limit).all()

    def get_one(self, tenant_id: int) -> Tenant:
        return self.session.query(Tenant).filter(
            Tenant.id == tenant_id).first()

    def get_by_name(self, name: str) -> Tenant:
        return self.session.query(Tenant).filter(Tenant.name == name).first()

    def get_by_subdomain(self, subdomain: str) -> Tenant:
        return self.session.query(Tenant).filter(Tenant.subdomain == subdomain).first()

    def update(self, update_tenant: Tenant) -> None:
        self.session.commit()
        self.session.refresh(update_tenant)

    def delete(self, tenant: Tenant) -> None:
        self.session.delete(tenant)
        self.session.commit()
        return None
