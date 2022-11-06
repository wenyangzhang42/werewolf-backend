from fastapi import APIRouter, Request, HTTPException

from app.services import game
from app.utils.response_utils import api_response, api_exception
from app.utils.log_utils import logger

logger_agent = 'Router'

router = APIRouter()


@router.get('/room1')
def welcome():
    result = {"message": "Welcome to Cat's Werewolf game! Please Setup to play!"}
    return api_response(result)


@router.get('/room1/test')
def test(roles):
    pass


@router.get('/room1/setup')
def setup(roles: str, request: Request):
    roles = roles.split(',')

    (code, result) = game.setup_game(roles)
    if "error" in result:
        logger.exception(result["error"])
        return api_exception(status_code=code, message=result['message'], error=result['error'])
    else:
        return api_response(result, code)


@router.get('/room1/restart')
def restart():
    (code, result) = game.restart_game()

    if "error" in result:
        logger.exception(result["error"])
        return api_exception(status_code=code, message=result['message'], error=result['error'])
    else:
        return api_response(result, code)


@router.get('/room1/reset')
def reset():
    (code, result) = game.reset_game()

    if "error" in result:
        logger.exception(result["error"])
        return api_exception(status_code=code, message=result['message'], error=result['error'])
    else:
        return api_response(result, code)


@router.get('/room1/sit/{seat}/{name}')
def set_player(seat: int, name: str):

    (code, result) = game.set_player(seat, name)

    if "error" in result:
        logger.exception(result["error"])
        return api_exception(status_code=code, message=result['message'], error=result['error'])
    else:
        return api_response(result, code)


@router.get('/room1/role/{name}')
def get_role(name: str):

    (code, result) = game.get_role(name)

    if "error" in result:
        logger.exception(result["error"])
        return api_exception(status_code=code, message=result['message'], error=result['error'])
    else:
        return api_response(result, code)


@router.get("/room1/start")
def start_game():
    (code, result) = game.start_game()

    if "error" in result:
        logger.exception(result["error"])
        return api_exception(status_code=code, message=result['message'], error=result['error'])
    else:
        return api_response(result, code)


@router.get('/room1/pre_ability/{name}')
def pre_check(name: str):

    (code, result) = game.pre_check(name)

    if "error" in result:
        logger.exception(result["error"])
        return api_exception(status_code=code, message=result['message'], error=result['error'])
    else:
        return api_response(result, code)


@router.get("/room1/ability/{player_role}/{player_seat}")
def use_ability(player_role: str, player_seat: str, targets: str, request: Request):

    (code, result) = game.use_ability(player_role, player_seat, targets)

    print(code)
    print(result)

    if "error" in result:
        logger.exception(result["error"])
        return api_exception(status_code=code, message=result['message'], error=result['error'])
    else:
        return api_response(result, code)


@router.get('/room1/night_info')
def night_info():
    (code, result) = game.get_night_info()

    if "error" in result:
        logger.exception(result["error"])
        return api_exception(status_code=code, message=result['message'], error=result['error'])
    else:
        return api_response(result, code)


@router.get('/room1/next_night')
def next_night(exiled: str, request: Request):
    (code, result) = game.next_night(exiled)

    if "error" in result:
        logger.exception(result["error"])
        return api_exception(status_code=code, message=result['message'], error=result['error'])
    else:
        return api_response(result, code)




