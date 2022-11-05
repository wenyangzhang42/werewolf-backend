from app.utils.log_utils import logger
from app.utils.game_utils import invoke
import app.services.game_info as gi


def setup_game(roles: list):
    try:
        gi.setup(roles)
    except Exception as e:
        logger.error("Error setting up the game!", e)
        return 500, {"message": "Cannot set roles for the game!", "error": e}
    logger.info(f"game set up with roles: {roles}")
    return 200, {"message": f"game setup with roles: {str(roles)}"}


def restart_game():
    try:
        gi.restart()
    except Exception as e:
        logger.error(f"Error restarting game, Error: {e}")
        return 500, {"message": "Error restarting game!", "error": e}
    logger.info(f"Game reset without changing configuration.")
    return 200, {"message": "Game successfully reset!"}


def reset_game():
    try:
        gi.reset()
    except Exception as e:
        logger.error(f"Error Clear game settings, Error: {e}")
        return 500, {"message": "Error Clear game settings,", "error": e}

    logger.info(f"Successfully cleared game settings.")
    return 200, {"message": "Successfully cleared game settings."}


def set_player(seat: int, ip: str):
    try:
        gi.set_player(seat, ip)
    except Exception as e:
        logger.error(f"Error setting player, Error: {e}")
        return 500, {"message": "Error setting player!", "error": e}

    logger.info(f"player {ip} sit on seat {seat}")
    return 200, {"message": f"You sit on seat {seat}!"}


def use_ability(ip: str, targets: str):
    # todo: maybe need to move this logic to game_info.py or put it in try block
    if not gi.game_is_configured():
        return 404, {"message": "Error using role ability!", "error": "game is not configured!"}

    try:
        targets = targets.split(',')
        while '' in targets:
            targets.remove('')
        targets = map(lambda x: int(x), targets)

        player = gi.find_player(ip)

        if player is None:
            return 403, {"message": f"You are not part of the game. Please wait for others to finish the game."}
        elif player.status != "alive":
            return 403, {"message": f"You are {player.status}. Please wait for others to finish the game."}
        stage = gi.get_stage()

        if stage != player.role:
            logger.warning(f"player {player.seat} trying to use skill where current stage is {stage}")
            return 403, {"message": "It is not your turn or you don't have an ability!", "error": "It is not your turn"}
        else:
            eval_result = invoke(player.role, player.seat, targets)
            next_stage = gi.move_to_next_stage()
            return 200, {"message": eval_result, "next_stage": next_stage}

    except Exception as e:
        return 500, {"message": f"Error suing ability!", "error": e}


def start_game():
    try:
        next_stage = gi.start_game()
    except Exception as e:
        return 500, {"message": "Error starting game!", "error": e}

    return 200, {"message": "Game started!", "next_stage": next_stage}


# Game Process Handlers
def get_night_info():
    try:
        night_info = gi.get_night_info()
    except Exception as e:
        return 500, {"message": f"Error getting last night info!", "error": e}

    return 200, {"message": "last night info: ", "night_info": night_info}


def next_night(exiled: str):
    try:
        exiled = exiled.split(',')
        while '' in exiled:
            exiled.remove('')
        exiled = map(lambda x: int(x), exiled)

        next_stage = gi.new_night(exiled)
    except Exception as e:
        return 500, {"message": "Error moving to next night!", "error": e}

    return 200, {"message": "Next night began!", "next_stage": next_stage}

