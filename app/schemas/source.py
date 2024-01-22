from pydantic import BaseModel, EmailStr
from uuid import UUID
from typing import Optional


class SourceBase(BaseModel):
    id: UUID
    title: str


class SourceDetaile(BaseModel):
    id: UUID
    title: str
    slug: Optional[str] = None


class SourceCreate(SourceBase):
    pass


class SourceUpdate(SourceBase):
    pass


class SourceInDB(SourceBase):
    id: UUID


class UserOut(SourceBase):
    pass
