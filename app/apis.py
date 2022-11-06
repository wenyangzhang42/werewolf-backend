from fastapi import APIRouter, Request, HTTPException

from app.services import game
from app.utils.response_utils import api_response, api_exception
from app.utils.log_utils import logger

logger_agent = 'Router'

router = APIRouter()


@router.get('/')
def welcome():
    result = {"message": "Welcome to Cat's Werewolf game! Please Setup to play!"}
    return api_response(result)


@router.get('/test')
def test(roles):
    pass


@router.get('/setup')
def setup(roles: str, request: Request):
    roles = roles.split(',')

    (code, result) = game.setup_game(roles)
    if "error" in result:
        logger.exception(result["error"])
        return api_exception(status_code=code, message=result['message'], error=result['error'])
    else:
        return api_response(result, code)


@router.get('/restart')
def restart():
    (code, result) = game.restart_game()

    if "error" in result:
        logger.exception(result["error"])
        return api_exception(status_code=code, message=result['message'], error=result['error'])
    else:
        return api_response(result, code)


@router.get('/reset')
def reset():
    (code, result) = game.reset_game()

    if "error" in result:
        logger.exception(result["error"])
        return api_exception(status_code=code, message=result['message'], error=result['error'])
    else:
        return api_response(result, code)


@router.get('/sit/{seat}/{name}')
def set_player(seat: int, name: str):

    (code, result) = game.set_player(seat, name)

    if "error" in result:
        logger.exception(result["error"])
        return api_exception(status_code=code, message=result['message'], error=result['error'])
    else:
        return api_response(result, code)


@router.get('/role/{name}')
def get_role(name: str):

    (code, result) = game.get_role(name)

    if "error" in result:
        logger.exception(result["error"])
        return api_exception(status_code=code, message=result['message'], error=result['error'])
    else:
        return api_response(result, code)


@router.get("/start")
def start_game():
    (code, result) = game.start_game()

    if "error" in result:
        logger.exception(result["error"])
        return api_exception(status_code=code, message=result['message'], error=result['error'])
    else:
        return api_response(result, code)


@router.get('/pre_ability/{name}')
def pre_check(name: str):

    (code, result) = game.pre_check(name)

    if "error" in result:
        logger.exception(result["error"])
        return api_exception(status_code=code, message=result['message'], error=result['error'])
    else:
        return api_response(result, code)


@router.get("/ability/{player_role}/{player_seat}")
def use_ability(player_role: str, player_seat: str, targets: str, request: Request):

    (code, result) = game.use_ability(player_role, player_seat, targets)

    print(code)
    print(result)

    if "error" in result:
        logger.exception(result["error"])
        return api_exception(status_code=code, message=result['message'], error=result['error'])
    else:
        return api_response(result, code)


@router.get('/night_info')
def night_info():
    (code, result) = game.get_night_info()

    if "error" in result:
        logger.exception(result["error"])
        return api_exception(status_code=code, message=result['message'], error=result['error'])
    else:
        return api_response(result, code)


@router.get('/next_night')
def next_night(exiled: str, request: Request):
    (code, result) = game.next_night(exiled)

    if "error" in result:
        logger.exception(result["error"])
        return api_exception(status_code=code, message=result['message'], error=result['error'])
    else:
        return api_response(result, code)




