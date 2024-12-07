from sqlmodel import Field, SQLModel
from datetime import date

class Coach(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    userid: int | None = Field(default=None, foreign_key="user.id")
    coachSince: date
    orgAssociated: list[int] | None
    sportAssociated: list[int] | None
    