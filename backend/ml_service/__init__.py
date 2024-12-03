from fastapi import APIRouter

from ml_service import handlers


ml_router = APIRouter(tags=["ML service"])
ml_router.include_router(handlers.router)
