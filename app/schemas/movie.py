from pydantic import BaseModel, UUID4
from typing import Optional


class MovieBase(BaseModel):
    id: UUID4
    title: str
    image: Optional[str] = None
    imdb_rating: Optional[float] = None
    tmdb_rating: Optional[float] = None
    kinopoisk_rating: Optional[float] = None


class MoveDetail(MovieBase):
    description: Optional[str] = None
    keywords: Optional[str] = None
    duration: Optional[str] = None


class MovieInDB(MovieBase):
    id: UUID4


class MovieCreate(MovieBase):
    pass


class MovieUpdate(MovieBase):
    pass


class Movie_Pydantic(MovieInDB):
    class Config:
        orm_mode = True
