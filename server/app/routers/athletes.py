from fastapi import APIRouter

router = APIRouter()

@router.get("/athletes/", tags=["athletes"])
async def read_athletes():
    return [{"athleteName": "Abdullah"}, {"athleteName": "Goku"}]

@router.get("/athletes/{name}", tags=["athletes"])
async def read_athlete_by_name(name: str):
    return {"specificAtheletebyName": "Abdullah"}

@router.get("/athletes/{id}", tags=["athletes"])
async def read_athlete_by_id(name: str):
    return {"specificAtheletebyId": "Abdullah"}

@router.get("/athletes/{orgName}", tags=["athletes"])
async def read_athletes_of_org(orgName: str):
    return {"athletesOfSpecificOrg": []}

@router.get("/athletes/{sport}", tags=["athletes"])
async def read_athletes_of_org(sportName: str):
    return {"athletesOfSpecificSport": []}