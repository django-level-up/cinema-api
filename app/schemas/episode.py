from pydantic import BaseModel, UUID4


class EpisodeBaseSchema(BaseModel):
    id: UUID4
    title: str
    description: str
    duration: str = None

class EpisodeDetailSchema(EpisodeBaseSchema):
    season_id: UUID4

class EpisodeInDB(BaseModel):
    id: UUID4
