import json

from fastapi import APIRouter

from . import handlers

from database.credentials import credentials_data, credentials_database_path
from database.onboarding import onboarding_data, users_onboarding_database_path


auth_router = APIRouter(tags=["Authentification service"])
auth_router.include_router(handlers.router)


@auth_router.on_event("shutdown")
async def shutdown_event():
    with open(credentials_database_path, "w") as json_file:
        json.dump(credentials_data, json_file)

    with open(users_onboarding_database_path, "w") as json_file:
        json.dump(onboarding_data, json_file)
