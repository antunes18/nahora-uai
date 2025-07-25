from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import relationship
from api.core.database import Base


class Tenant(Base):
    __tablename__ = "tenants"
    id: int = Column(Integer, primary_key=True,
                     nullable=False, autoincrement=True)
    name: str = Column(String, unique=True)
    subdomain: str = Column(String, unique=True)
    logo_url: str = Column(String)
    primary_color: str = Column(String)

    users = relationship("User", back_populates="tenant")
