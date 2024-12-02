from fastapi import APIRouter

router = APIRouter()

@router.get("/organizations/", tags=["organizations"])
async def read_users():
    return [{"orgNameame": "Abdullah"}, {"orgName": "Goku"}]

@router.get("/organizations/{orgName}", tags=["organizations"])
async def read_user(orgName: str):
    return {"orgName": orgName}