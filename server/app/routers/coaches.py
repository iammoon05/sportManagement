from fastapi import APIRouter

router = APIRouter()

@router.get("/coaches/", tags=["coaches"])
async def read_athletes():
    return [{"coachName": "Abdullah"}, {"coachName": "Goku"}]

@router.get("/coaches/{name}", tags=["coaches"])
async def read_coach_by_name(name: str):
    return {"specificCoachbyName": "Abdullah"}

@router.get("/coaches/{id}", tags=["coaches"])
async def read_coach_by_id(name: str):
    return {"specificCoachbyId": "Abdullah"}

@router.get("/coaches/{orgName}", tags=["coaches"])
async def read_coaches_of_org(orgName: str):
    return {"coachesOfSpecificOrg": []}

@router.get("/coaches/{sport}", tags=["coaches"])
async def read_coaches_of_org(sportName: str):
    return {"coachesOfSpecificSport": []}