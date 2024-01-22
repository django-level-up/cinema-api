from fastapi import APIRouter, HTTPException
from models import (
    Movie,
    MovieSource,
)
from schemas import (
    MovieBaseSchema,
    MovieDetailSchema,
    MovieSourceBaseSchema,
)
from typing import List
from uuid import UUID

router = APIRouter()


@router.get("/movies", response_model=List[MovieBaseSchema])
async def read_all_movies():
    movies = await Movie.all().values()
    return movies


@router.get("/movies/{movie_id}", response_model=MovieDetailSchema)
async def read_movie(movie_id: UUID):
    movie = await Movie.get_or_none(id=movie_id).values()
    if movie:
        return movie[0]
    raise HTTPException(status_code=404, detail="Movie not found")


@router.get("/movies/{movie_id}/sources", response_model=List[MovieSourceBaseSchema])
async def read_movie_sources(movie_id: UUID):
    movie_source = await MovieSource.filter(movie=movie_id).values()
    if movie_source:
        return movie_source
    raise HTTPException(status_code=404, detail="No sources was found")
