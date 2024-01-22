from fastapi import APIRouter, HTTPException
from models import (
    Show,
    Season,
)
from schemas import (
    ShowBaseSchema,
    ShowDetailSchema,
    SeasonBaseSchema,
)
from typing import List
from uuid import UUID

router = APIRouter()


@router.get("/shows", response_model=List[ShowBaseSchema])
async def read_all_shows():
    shows = await Show.all().values()
    return shows


@router.get("/shows/{show_id}", response_model=ShowDetailSchema)
async def read_show(show_id: UUID):
    show = await Show.get_or_none(id=show_id).values()
    if show:
        return show[0]
    raise HTTPException(status_code=404, detail="Show not found")


@router.get("/shows/{show_id}/seasons", response_model=List[SeasonBaseSchema])
async def read_show_seasons(show_id: UUID):
    seasons = await Season.filter(show=show_id).values()
    if seasons:
        return seasons
    raise HTTPException(status_code=404, detail="No season was found")
