import random

from app.models.game_infos import game_info_model, night_info_model, every_night_order_model, first_night_order_model
from app.models.player import Player
from app.utils.loggers import logger
from app.utils.info_utils import validate_roles, find_alignment

# parameters for the room
nbr_of_players = 0
every_night_order = []
first_night_order = []

# parameters for each game
roles = []
players = []
game_on_going = False
game_start_datetime = None
game_info = game_info_model.copy()
night_info = night_info_model.copy()


def setup(roles_to_set: list):
    (validated, msg) = validate_roles(roles_to_set)
    if not validated:
        raise Exception(msg)

    # If room is not cleared yet. rest() to clear room.
    global nbr_of_players
    if nbr_of_players != 0:
        reset()  # maybe a better way is to reset params for each game here.

    global roles, players, first_night_order, every_night_order, \
        game_info, night_info, game_on_going, game_start_datetime
    roles = roles_to_set.copy()
    random.shuffle(roles)
    for role in first_night_order_model:
        if role in roles:
            first_night_order.append(role)
    for role in every_night_order_model:
        if role in roles:
            first_night_order.append(role)
            every_night_order.append(role)
    nbr_of_players = len(roles)
    players = [None]*nbr_of_players
    logger.debug(f"successfully set roles {roles}")
    logger.debug(f"successfully set first night order: {first_night_order}")
    logger.debug(f"successfully set every night order: {every_night_order}")
    logger.debug(f"successfully set empty players list: {players}")


def restart() -> None:
    global roles, players, game_info, night_info, game_on_going, game_start_datetime
    random.shuffle(roles)
    game_on_going = False
    game_start_datetime = None
    try:
        for i in range(nbr_of_players):
            players[i].set_role(roles[i])
            players[i].set_status("alive")
        game_info = game_info_model.copy()
        night_info = night_info_model.copy()
    except Exception as e:
        raise Exception("Unknown Error resetting player roles and status.")
    logger.debug("Game has been reset without changing setups!")


def reset() -> None:
    global roles, players, nbr_of_players, first_night_order, every_night_order,\
        game_info, night_info, game_on_going, game_start_datetime
    nbr_of_players = 0
    game_on_going = False
    game_start_datetime = None
    roles = []
    players = []

    game_info = game_info_model.copy()
    night_info = night_info_model.copy()
    first_night_order = []
    every_night_order = []

    logger.debug("Game successfully reset.")


def set_game_info(field, value):
    global game_info
    game_info[field] = value


def set_night_info(field, value):
    global night_info
    night_info[field] = value


def set_player(seat: int, ip: str):
    global players
    current_player = find_player(ip)
    if current_player is not None:
        raise Exception(f"You have already sit on number {current_player.seat+1}")
    try:
        if players[seat-1] is not None:
            raise Exception(f"Seat {seat} has been taken.")
        else:
            role = roles[seat - 1]
            alignment = find_alignment(role)
            player = Player(ip, seat, role, alignment)
            players[seat-1] = player
            logger.debug("Player " + ip + " seated at seat " + str(seat))
    except Exception as e:
        raise Exception(f"Unknown error set player {ip} at seat {seat}. exception: {e}")


# Helper functions
def find_player(ip: str):
    global players
    for player in players:
        if player is not None and player.ip == ip:
            return player
    return None


def get_stage() -> str:
    global game_info, night_info
    if game_info.get("round") == 0:
        raise Exception("Game not set or game not started!")
    elif game_info.get("round") == 1:
        global first_night_order
        return first_night_order[night_info.get("stage")]
    else:
        global every_night_order
        return every_night_order[night_info.get("stage")]


def game_is_configured() -> bool:
    global nbr_of_players
    if nbr_of_players == 0:
        return False
        # raise Exception("Game is not configured yet!")
    return True


def debug_print():  # This will log and print out all current game info for debug uses.
    global roles, players, nbr_of_players, first_night_order, every_night_order, \
        game_info, night_info, game_on_going, game_start_datetime
    print(f"==== DEBUG PRINT START ====")
    print(f"Current roles: {roles}")
    print(f"Current players: {players}")
    print(f"Current game info: {game_info}")
    print(f"Current night info: {night_info}")

    logger.debug(f"==== DEBUG PRINT START ====")
    logger.debug(f"Current roles: {roles}")
    logger.debug(f"Current players: {players}")
    logger.debug(f"Current game info: {game_info}")
    logger.debug(f"Current night info: {night_info}")