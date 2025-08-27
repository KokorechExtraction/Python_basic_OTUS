from fastapi import APIRouter


from api.api_v2 import router as api_v2

router = APIRouter(prefix="/api", tags=["API"])


router.include_router(api_v2)
