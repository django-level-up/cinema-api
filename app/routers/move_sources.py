from fastapi import APIRouter, HTTPException
from app.models import Source, MovieSource
from app.schemas import MovieSourceBase
from uuid import UUID
from typing import List

router = APIRouter()


@router.get("/movie_sources/", response_model=MovieSourceBase)
async def get_movie_sources():
    source = await MovieSource.all()
    if source is not None:
        return source
    raise HTTPException(status_code=404, detail="not found")


# @router.get("/movies_sources/{movie_id}", response_model=List[MovieSourceBase])
# async def get_movie_sources(movie_id: UUID):
#     movie_sources = await MovieSource.filter(movie_id=movie_id).all()
#     if movie_sources:
#         return [await MovieSource.from_orm(movie_source) for movie_source in movie_sources]
#     raise HTTPException(status_code=404, detail=f"Movie with id {movie_id} not found")

