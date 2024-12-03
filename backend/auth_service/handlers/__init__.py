from fastapi import APIRouter

from . import auth
from . import onboarding


router = APIRouter()

router.include_router(auth.router)
router.include_router(onboarding.router)
