from pydantic import BaseModel, EmailStr
from datetime import date

class AthleteBase(BaseModel):
    userid: int

class Awards(BaseModel):
    awardName: str
    date: date
    
class AthleteOut(AthleteBase):
    athleteSince: date
    orgAssociated: list[int]
    sportAssociated: list[int]
    awards: list[Awards]
    results: list
    
