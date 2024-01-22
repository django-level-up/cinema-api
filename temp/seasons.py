from fastapi import APIRouter, HTTPException, Path
from uuid import UUID
import httpx

from app import config
DRF_BASE_URL = config.DRF_BASE_URL

router = APIRouter()


@router.get("/api/v1/content/seasons/")
async def get_drf_seasons():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{DRF_BASE_URL}/api/v1/content/seasons/")
            response.raise_for_status()
            data = response.json()
            return data
    except httpx.HTTPError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


@router.get("/api/v1/content/seasons/{id}")
async def get_drf_season(
    id: UUID = Path(..., title="The UUID of the show to retrieve"),
):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{DRF_BASE_URL}/api/v1/content/seasons/{id}/")
            response.raise_for_status()
            data = response.json()
            return data
    except httpx.HTTPError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
