from fastapi import APIRouter, HTTPException
from models.source import Source
from schemas.source import SourceBaseSchema
from typing import List
from uuid import UUID

router = APIRouter()


@router.get("/sources", response_model=List[SourceBaseSchema])
async def read_all_sources():
    sources = await Source.all().values()
    return sources


@router.get("/sources/{source_id}", response_model=SourceBaseSchema)
async def read_source(source_id: UUID):
    source = await Source.get_or_none(id=source_id).values()
    if source is None:
        raise HTTPException(status_code=404, detail="Source not found")
    return source[0]
