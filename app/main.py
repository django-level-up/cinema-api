from fastapi import FastAPI
from routers import (
    movie,
    move_sources,
    source,
    show,
    season,
    episode,
)
from tortoise.contrib.fastapi import register_tortoise
from config import TORTOISE_ORM

app = FastAPI()

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)

app.include_router(movie.router)
app.include_router(show.router)
app.include_router(season.router)
app.include_router(episode.router)


app.include_router(source.router)
app.include_router(move_sources.router)
