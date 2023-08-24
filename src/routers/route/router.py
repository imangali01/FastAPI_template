from fastapi import APIRouter, HTTPException

from . import utils, services



router = APIRouter(
    prefix='/route',
    tags=['Route']
)


@router.get("/")
async def hello():
    '''Print hallo'''
    kwargs = {}

    return await services.Hello.print(**kwargs)