from fastapi import APIRouter

import handlers


ml_router = APIRouter(tags=["ML service"])
ml_router.include_router(handlers.router)
