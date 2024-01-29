from fastapi import APIRouter
from routes.auth import auth_router

router = APIRouter()
router.include_router(auth_router,prefix="/web",tags=["admin"])