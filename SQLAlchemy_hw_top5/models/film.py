from typing import List
from sqlalchemy import String, Column, Integer, Date
from .base import Base
from sqlalchemy.orm import Mapped, relationship
from .genre import Genre
from .associates import films_genres_assoc_table

class Film(Base):
    __tablename__ = "films"
    id = Column(Integer, primary_key=True)
    author = Column(String(50))
    description = Column(String(300))
    year = Column(Date)

    genre:Mapped[List[Genre]]= relationship(secondary=films_genres_assoc_table)