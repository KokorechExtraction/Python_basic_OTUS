from fastapi import APIRouter
from api.api_v2.users.view import router as users_router
from api.api_v2.posts.view import router as posts_router

router = APIRouter(prefix="/v2", tags=["V1"])

router.include_router(users_router)
router.include_router(posts_router)
