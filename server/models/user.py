from sqlmodel import Field, SQLModel
from datetime import date

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    email: str
    firstName: str
    middleName: str | None
    lastName: str
    birthYear: int
    birthMonth: int
    birthDay: int
    birthCountry: str
    nationality: str
    currentCity: str
    postalCode: int
    hashed_password: str
    created_at: date
    last_updated: date
    