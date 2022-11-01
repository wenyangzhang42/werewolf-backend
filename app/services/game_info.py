import random

from app.models.game_infos import game_info_model, night_info_model
from app.models.player import Player
from app.utils.other_utils import find_alignment
from app.utils.loggers import logger


nbr_of_players = 0
game_start_datetime = None
roles = []
players = []
game_info = game_info_model.copy()
night_info = night_info_model.copy()


def reset():
    global nbr_of_players, roles, players, game_info, night_info
    nbr_of_players = 0
    roles = []
    players = []
    game_info = game_info_model.copy()
    night_info = night_info_model.copy()

    logger.warning("Game re-initialized!")
    return 200, "Game ended, please setup game to play!"


def restart():
    global nbr_of_players
    if nbr_of_players == 0:
        return 500, "game is not setup, cannot restart."
        logger.warning("Cannot start game before setup")
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
            logger.error("Unknown Error resetting player roles and status.")
            return 500, "Unknown Error resetting player roles and status."
        logger.warning("Game has been reset without changing setups!")
        return 200, "Players' roles shuffled, You may start another game now!"


def set_roles(role_list: list):
    if role_list is None or len(role_list) == 0:
        logger.warning("Empty or Null input for roles list.")
        return 500, "Input roles list is empty!"
    global roles
    roles = role_list.copy()
    random.shuffle(roles)
    logger.info("Game roles set: " + str(roles))
    return 200, "Game roles set."


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
        logger.warning("Player " + ip + " tried to pick seat " + seat + " when game is not set up.")
        return 500, "Game has not been setup yet."
    try:
        if players[seat-1] is not None:
            logger.warning("Player " + ip + " tried to pick seat " + seat + " which is already taken.")
            return 500, "Seat has been taken."
        else:
            role = roles[seat - 1]
            alignment = find_alignment(role)
            player = Player(ip, seat, role, alignment)
            player[seat-1] = player
            logger.info("Player " + ip + " seated at seat " + str(seat))
            return 200, "player seated at seat " + str(seat)
    except Exception as e:
        logger.error("Player " + ip + " tried to pick seat " + seat + " available seats are 1-" + str(nbr_of_players))
        return 500, "seat number out of range. please pick seat between 1-"+str(nbr_of_players)
