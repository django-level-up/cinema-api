from pydantic import BaseModel, UUID4



class EpisodeSourceBaseSchema(BaseModel):
    episode_id: UUID4
    source_id: UUID4
    download_link: str = None
    kinopoisk_link: str = None
    imdb_link: str = None
    valid_source: bool = True


class EpisodeSourceCreateSchema(EpisodeSourceBaseSchema):
    pass


class EpisodeSourceUpdateSchema(EpisodeSourceBaseSchema):
    pass


class EpisodeSourceInDB(EpisodeSourceBaseSchema):
    id: UUID4
