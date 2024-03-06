from fastapi import APIRouter

router = APIRouter(
    tags=["ping"],
    responses={200: {"description": "Successful Response"}},
)

@router.get("/ping")
async def ping():
    return "pong"