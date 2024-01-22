from fastapi import APIRouter, HTTPException
from app.models.movie import Movie
from app.models.source import Source
from app.schemas.movie import MovieBase, MoveDetail
from uuid import UUID
from typing import List

router = APIRouter()

@router.get("/movies/{movie_id}", response_model=MoveDetail)
async def get_movie(movie_id: UUID): 
    movie = await Movie.get_or_none(id=movie_id)
    if movie is not None:
        return await movie
    raise HTTPException(status_code=404, detail=f"Movie with id {movie_id} not found")


@router.get("/movies", response_model=List[MovieBase])
async def get_all_movies():
    movies = await Movie.all()
    return movies
