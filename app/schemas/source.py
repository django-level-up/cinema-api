from pydantic import BaseModel
from uuid import UUID


class SourceBaseSchema(BaseModel):
    id: UUID
    title: str = None
    slug: str = None
