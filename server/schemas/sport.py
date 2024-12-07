from pydantic import BaseModel, EmailStr
from datetime import date

class SportBase(BaseModel):
    pass

class SportOut(SportBase):
    id: int
    totalOrganizations: int
    totalAthletes: int
    totalCoaches: int
    totalCompetitions: int
    orgAssociated: list[int] | None = None
    sportAssociated: list[int] | None = None