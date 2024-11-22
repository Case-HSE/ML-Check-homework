from fastapi import APIRouter

from . import ai
from . import workchecking

router = APIRouter()

router.include_router(ai.router)
router.include_router(workchecking.router)


@router.get("/")
async def starting_page():
    return "ZOV"
