from sqlalchemy import Column, BigInteger, String, DateTime, func, Integer
from src.services.db.base import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(BigInteger, primary_key=True)
    username = Column(String(50))
    fullname = Column(String(50))
    time_created = Column(DateTime(timezone=True), server_default=func.now())
