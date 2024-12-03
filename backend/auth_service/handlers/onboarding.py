from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasicCredentials
from typing import Annotated

from .auth import security

from auth_service.database.onboarding import onboarding_data
from auth_service.models import OnBoardingModel, StatusModel


router = APIRouter(prefix="/onboarding")


@router.post("/set_data")
async def set_onboarding_data(
        body: OnBoardingModel,
        credentials: Annotated[HTTPBasicCredentials, Depends(security)]
) -> StatusModel:

    onboarding_data[credentials.username] = body.model_dump_json()
    return StatusModel()
