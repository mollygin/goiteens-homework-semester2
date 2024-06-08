from sqlalchemy import Integer, String, Column
from .base import Base

class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))