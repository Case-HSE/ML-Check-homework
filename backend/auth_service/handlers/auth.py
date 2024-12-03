from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Annotated

from auth_service.utils.hash import get_hash

from auth_service.database.credentials import credentials_data

from auth_service.exceptions import wrong_login_password_ex
from auth_service.models import AddAccountModel, StatusModel


router = APIRouter(prefix="/auth")

security = HTTPBasic()


@router.post("/add-account")
async def add_account(body: AddAccountModel) -> StatusModel:
    hash_password = get_hash(hash_object=body.password)
    credentials_data[body.username] = hash_password
    return StatusModel()


@router.get("/basic-auth")
async def check_auth(
        credentials: Annotated[HTTPBasicCredentials, Depends(security)]
) -> StatusModel:
    hash_password = get_hash(hash_object=credentials.password)
    try:
        assert credentials.username in credentials_data
        assert credentials_data[credentials.username] == hash_password
    except AssertionError:
        raise wrong_login_password_ex

    return StatusModel()
