from fastapi import APIRouter
from models import MovieSource
from schemas import (
    MovieSourceBaseSchema,
)
from uuid import UUID
from typing import List

router = APIRouter()


@router.get("/movie_sources", response_model=List[MovieSourceBaseSchema])
async def read_all_sources():
    movie_sources = await MovieSource.all().values()
    return movie_sources


@router.get("/movie_sources/{source_id}", response_model=MovieSourceBaseSchema)
async def get_movie_sources(source_id: UUID):
    movie_source = await MovieSource.get_or_none(id=source_id).values()
    return movie_source[0]
