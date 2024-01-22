# main.py
from fastapi import FastAPI
from app.routers import user, movie, source, move_sources
from tortoise.contrib.fastapi import register_tortoise
from app.config import TORTOISE_ORM

app = FastAPI()

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)

app.include_router(user.router)
app.include_router(movie.router)
app.include_router(source.router)
app.include_router(move_sources.router)


