# app/routers/user.py
from fastapi import APIRouter, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from app.models.user import User
from app.schemas.user import UserInDB
from uuid import UUID


router = APIRouter()

@router.get("/users/{user_id}", response_model=UserInDB)
async def get_user(user_id: UUID):
    user = await User.get_or_none(id=user_id)
    if user is not None:
        return user
    raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")

@router.get("/users", response_model=list[UserInDB])
async def get_all_users():
    users = await User.all()
    return users
