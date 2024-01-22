from pydantic import BaseModel, EmailStr
from uuid import UUID
class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserInDB(UserBase):
    id: UUID

class UserOut(UserInDB):
    pass
