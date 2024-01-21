from fastapi import APIRouter, HTTPException, Path
from uuid import UUID
import httpx

from app import config

DRF_BASE_URL = config.DRF_BASE_URL

router = APIRouter()


@router.get("/api/v1/content/episodes/")
async def get_drf_episodes():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{DRF_BASE_URL}/api/v1/content/episodes/")
            response.raise_for_status()
            data = response.json()
            return data
    except httpx.HTTPError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


@router.get("/api/v1/content/episodes/{id}")
async def get_drf_episode(
    id: UUID = Path(..., title="The UUID of the show to retrieve"),
):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{DRF_BASE_URL}/api/v1/content/episodes/{id}/")
            response.raise_for_status()
            data = response.json()
            return data
    except httpx.HTTPError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
