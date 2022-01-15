from asyncio import streams
from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    firstName: str
    lastName: str


class UserInDBSchema(UserSchema):
    password: str

