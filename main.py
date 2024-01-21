from fastapi import FastAPI
from app.routers import (
    movies,
    shows,
    seasons,
    episodes,
)

app = FastAPI()

app.include_router(movies.router)
app.include_router(shows.router)
app.include_router(seasons.router)
app.include_router(episodes.router)
