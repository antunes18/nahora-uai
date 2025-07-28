from sqlalchemy import Column, String, Integer, Float
from api.core.database import Base


class Plan(Base):
    __tablename__ = "plans"
    id: Integer = Column(Integer, primary_key=True, autoincrement=True)
    name: String = Column(String, unique=True)
    price: Float = Column(Float, default=0.0)
    user_limit: Integer = Column(Integer, default=0)
    scheduling_limit: Integer = Column(Integer, default=0)
