from sqlmodel import Field, SQLModel
from datetime import date

class Sport(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    totalOrganizations: int | None
    totalAtheltes: int | None
    totalCoaches: int | None
    orgAssociated: list[int] | None
    sportAssociated: list[int] | None
    