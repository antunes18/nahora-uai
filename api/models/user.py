from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from api.core.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    username: str = Column(String, unique=True, nullable=False)
    phone: str = Column(String, unique=True, nullable=True)
    email: str = Column(String, unique=True, nullable=False)
    password: str = Column(String, unique=False, nullable=False)
    role: str = Column(String, unique=False, nullable=False)
    disabled: bool = Column(Boolean, default=False)

    scheduling = relationship("Scheduling", back_populates="user")
    tenant_id: int | None = Column(ForeignKey("tenants.id"))
