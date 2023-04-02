from sqlalchemy import Column, String, Boolean, Integer
from config import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, index=True, unique=True)
    address = Column(String, index=True, unique=True)
    role = Column(String, index=True)
    premium = Column(Boolean, index=True)
    promotional = Column(Boolean, index=True)
    points = Column(Integer, index=True)
