from fastapi import APIRouter
from app.apis import router as api_router

router = APIRouter()

router.include_router(api_router)
