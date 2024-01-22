from pydantic import BaseModel, UUID4
from typing import Optional


class MovieSourceBaseSchema(BaseModel):
    id: UUID4
    movie_id: UUID4 = None
    source_id: UUID4 = None
    download_link: Optional[str] = None
    kinopoisk_link: Optional[str] = None
    imdb_link: Optional[str] = None
    tmdb_link: Optional[str] = None
    watch_link: Optional[str] = None
    valid_source: Optional[bool] = None


# class MovieSourceListSchema(BaseModel):
#     items: List[MovieSourceBaseSchema]

#     class Config:
#         orm_mode = True
