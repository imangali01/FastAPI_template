from fastapi import APIRouter, Depends

from .route.router import router as hello_router



router = APIRouter(
    prefix='/api',
    include_in_schema=True
)

router.include_router(hello_router)
