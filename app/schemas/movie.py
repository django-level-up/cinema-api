from pydantic import BaseModel, UUID4
from typing import Optional
from datetime import date


class MovieBaseSchema(BaseModel):
    id: UUID4
    title: str
    image: str = None
    imdb_rating: float = None
    tmdb_rating: float = None
    kinopoisk_rating: Optional[float] = None
    imdb_rating: Optional[float] = None
    tmdb_rating: Optional[float] = None


class MovieDetailSchema(MovieBaseSchema):
    bg_image: str = None
    duration: str = None
    keywords: str = None
    release_date: date = None


class MovieInDB(BaseModel):
    id: UUID4
