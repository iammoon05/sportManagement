from fastapi import APIRouter

router = APIRouter()

@router.get("/sports/", tags=["sports"])
async def read_sports():
    return [{"sportName": "Badminton"}, {"sportName": "Archery"}]

@router.get("/sports/{sportName}", tags=["sports"])
async def read_sport(sportName: str):
    return {"sportName": "some description about this sport"}