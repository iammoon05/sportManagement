from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr
    firstName: str | None = None
    lastName: str | None = None
    birthYear: int
    birthMonth: int
    birthDay: int
    birthCountry: str
    nationality: str
    currentCity: str
    postalCode: int
    
class UserIn(UserBase):
    password: str

class UserOut(UserBase):
    id: int

class UserInDb(UserBase):
    hashed_password: str