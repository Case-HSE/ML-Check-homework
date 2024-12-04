from fastapi import APIRouter

from . import auth
from . import onboarding
from . import subjects


router = APIRouter()

router.include_router(auth.router)
router.include_router(onboarding.router)
router.include_router(subjects.router)
