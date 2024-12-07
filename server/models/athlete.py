from sqlmodel import Field, SQLModel
from datetime import date

class Athlete(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    userid: int | None = Field(default=None, foreign_key="user.id")
    athleteSince: date
    orgAssociated: list[int]
    sportAssociated: list[int]
    awards: list[str]
    results: list[str]
    