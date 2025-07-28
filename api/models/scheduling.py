from sqlalchemy import Column, Integer, DateTime, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


from api.core.database import Base


class Scheduling(Base):
    __tablename__ = "scheduling"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tenant_id = Column(ForeignKey("tenants.id"))
    hour = Column(Integer, nullable=False)
    date = Column(DateTime(timezone=True), nullable=False)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    user_id = Column(ForeignKey("users.id"))
    is_deleted = Column(Boolean, default=False)

    user = relationship("User", back_populates="scheduling")
    tenant = relationship("Tenant", back_populates="schedulings")
