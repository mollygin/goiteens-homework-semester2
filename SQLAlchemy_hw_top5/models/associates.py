from sqlalchemy import Table, Column, ForeignKey
from .base import Base

films_genres_assoc_table = Table(
    "films_genres_assoc_table",
    Base.metadata,
    Column(
        "genre_id",
        ForeignKey("genres.id"),
        primary_key=True
    ),
    Column(
        "film_id",
        ForeignKey("films.id"),
        primary_key=True
    )
)