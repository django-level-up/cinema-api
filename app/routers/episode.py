from fastapi import APIRouter, HTTPException
from models import (
    Episode,
    EpisodeSource,
)
from schemas import (
    EpisodeBaseSchema,
    EpisodeSourceBaseSchema,
)
from typing import List
from uuid import UUID

router = APIRouter()


@router.get("/episodes", response_model=List[EpisodeBaseSchema])
async def read_all_episodes():
    episodes = await Episode.all().values()
    return episodes


@router.get("/episodes/{episode_id}", response_model=EpisodeBaseSchema)
async def read_episode(episode_id: UUID):
    episode = await Episode.get_or_none(id=episode_id).values()
    if episode:
        return episode[0]
    raise HTTPException(status_code=404, detail="Episode not found")


@router.get("/episodes/{episode_id}/sources", response_model=List[EpisodeSourceBaseSchema])
async def read_episode_sources(episode_id: UUID):
    source = await EpisodeSource.filter(episode=episode_id).values()
    if source:
        return source
    raise HTTPException(status_code=404, detail="No source was found")
