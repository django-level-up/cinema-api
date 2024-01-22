from fastapi import APIRouter, HTTPException
from models import (
    Season,
    Episode,
)
from schemas import (
    SeasonBaseSchema,
    EpisodeBaseSchema,
)
from typing import List
from uuid import UUID

router = APIRouter()


@router.get("/seasons", response_model=List[SeasonBaseSchema])
async def read_all_seasons():
    seasons = await Season.all().values()
    return seasons


@router.get("/seasons/{season_id}", response_model=SeasonBaseSchema)
async def read_season(season_id: UUID):
    season = await Season.get_or_none(id=season_id).values()
    if season:
        return season[0]
    raise HTTPException(status_code=404, detail="Season not found")


@router.get("/seasons/{season_id}/episodes", response_model=List[EpisodeBaseSchema])
async def read_season_episode(season_id: UUID):
    episodes = await Episode.filter(season=season_id).values()
    if episodes:
        return episodes
    raise HTTPException(status_code=404, detail="No episode was found")
