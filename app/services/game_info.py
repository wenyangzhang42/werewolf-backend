import random

from app.models.game_infos import game_info_model, night_info_model, every_night_order, first_night_order
from app.models.player import Player
from app.utils.info_utils import validate_roles
from app.utils.other_utils import find_alignment
from app.utils.loggers import logger


nbr_of_players = 0
game_on_going = False
game_start_datetime = None
roles = []
players = []
game_info = game_info_model.copy()
night_info = night_info_model.copy()

cur_every_night_order = []
cur_first_night_order = []


def setup(role_list: list):
    (validated, msg) = validate_roles(role_list)
    if not validated:
        raise Exception(msg)

    global roles, cur_first_night_order, cur_every_night_order
    roles = role_list.copy()
    random.shuffle(roles)
    for role in first_night_order:
        if role in roles:
            cur_first_night_order.append(role)
    for role in every_night_order:
        if role in roles:
            cur_every_night_order.append(role)
    logger.debug(f"successfully set roles {roles}")
    logger.debug(f"successfully set first night order: {cur_first_night_order}")
    logger.debug(f"successfully set every night order: {cur_every_night_order}")


def reset() -> None:
    global nbr_of_players, game_on_going, game_start_datetime, roles, players, \
        game_info, night_info, cur_first_night_order, cur_every_night_order
    nbr_of_players = 0
    game_on_going = False
    game_start_datetime = None
    roles = []
    players = []

    game_info = game_info_model.copy()
    night_info = night_info_model.copy()
    cur_first_night_order = []
    cur_every_night_order = []

    logger.debug("Game successfully reset.")


def restart() -> None:
    global nbr_of_players
    if nbr_of_players == 0:
        raise Exception("Cannot restart game, Game not set up.")
    else:
        global roles, players, game_info, night_info
        random.shuffle(roles)
        try:
            for i in range(nbr_of_players):
                players[i].set_role(roles[i])
                players[i].set_status("alive")
            game_info = game_info_model.copy()
            night_info = night_info_model.copy()
        except Exception as e:
            raise Exception("Unknown Error resetting player roles and status.")
        logger.debug("Game has been reset without changing setups!")


def set_nbr_of_players(count: int):
    global nbr_of_players
    nbr_of_players = count


def set_game_info(field, value):
    global game_info
    game_info[field] = value


def set_night_info(field, value):
    global night_info
    night_info[field] = value


def set_player(seat: int, ip: str):
    global nbr_of_players, players
    if nbr_of_players == 0:
        raise Exception(" Game has not been setup yet.")
    try:
        if players[seat-1] is not None:
            raise Exception(f"Seat {seat} has been taken.")
        else:
            role = roles[seat - 1]
            alignment = find_alignment(role)
            player = Player(ip, seat, role, alignment)
            player[seat-1] = player
            logger.debug("Player " + ip + " seated at seat " + str(seat))
    except Exception as e:
        raise Exception(f"Error set player {ip} at seat {seat}. exception: {e}")
