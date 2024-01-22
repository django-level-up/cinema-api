from pydantic import BaseModel, UUID4
from typing import Optional
from .movie import MovieBase
from .source import SourceBase
from uuid import UUID


class MovieSourceBase(BaseModel):
    id: UUID
    # movie: MovieBase
    source: SourceBase
    # download_link: str
    # kinopoisk_link: Optional[str] = None
    # imdb_link: Optional[str] = None
    # tmdb_link: Optional[str] = None
    # watch_link: Optional[str] = None
    # valid_source: bool


class MovieSourceCreate(MovieSourceBase):
    pass


class MovieSourceUpdate(MovieSourceBase):
    pass


class MovieSource_Pydantic(MovieSourceBase):
    class Config:
        orm_mode = True
