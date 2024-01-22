from pydantic import BaseModel, UUID4


class SeasonBaseSchema(BaseModel):
    id: UUID4
    title: str
    description: str
    duration: str = None

class SeasonDetailSchema(SeasonBaseSchema):
    show_id: UUID4

class SeasonInDB(BaseModel):
    id: UUID4
