from fastapi import APIRouter, HTTPException
from app.models import Source
from app.schemas import SourceBase, SourceDetaile
from uuid import UUID


router = APIRouter()


@router.get("/sources/{source_id}", response_model=SourceDetaile)
async def get_source(source_id: UUID):
    source = await Source.get_or_none(id=source_id)
    if source is not None:
        return source
    raise HTTPException(status_code=404, detail=f"source with id {source_id} not found")


@router.get("/sources", response_model=list[SourceBase])
async def get_all_sources():
    source = await Source.all()
    return source
