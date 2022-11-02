from fastapi import APIRouter, Request, HTTPException

from app.services.game import setup_game
from app.utils.response_utils import api_response, api_exception
from app.utils.loggers import logger

logger_agent = 'Router'

router = APIRouter()


@router.get('/')
def welcome():
    result = {"message": "Welcome to Cat's Werewolf game! Please Setup to play!"}
    return api_response(result)


@router.get('/test')
def test(roles):
    print(type(roles))
    print(roles)
    ls = roles.split(",")
    print(ls)
    print(len(ls))


@router.get('/setup')
def setup(roles: list, request: Request):
    roles = roles.split(',')
    (code, result) = setup_game(roles)
    if "error" in result:
        logger.exception(result["error"])
        api_exception(status_code=code, error_message=result['message'])
    else:
        return api_response(result)
