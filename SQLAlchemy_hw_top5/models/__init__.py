from models.base import (
    Session,
    Base,
    engine,
    create_db,
    drop_db
)

from models.film import(
    Genre,
    Film,
    films_genres_assoc_table
)

create_db()