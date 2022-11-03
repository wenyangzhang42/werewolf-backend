from app.utils.loggers import logger
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
    if not gi.game_is_configured():
        return 404, {"message": "Error restarting game!", "error": "game is not configured!"}
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
    if not gi.game_is_configured():
        return 404, {"message": "Error setting player!", "error": "game is not configured!"}
    try:
        gi.set_player(seat, ip)
    except Exception as e:
        logger.error(f"Error setting player, Error: {e}")
        return 500, {"message": "Error setting player!", "error": e}
    logger.info(f"player {ip} sit on seat {seat}")
    return 200, {"message": f"player {ip} sit on seat {seat}"}


def use_ability(target: int, ip: str):
    if not gi.game_is_configured():
        return 404, {"message": "Error using role ability!", "error": "game is not configured!"}
    try:
        player = gi.find_player(ip)
        if player.status != "alive":
            return 403, {"message": f"You are {player.status}. Please wait for others to finish the game."}
        stage = gi.get_stage()
        if stage != player.role:
            logger.warning(f"player {player.seat} trying to use skill where current stage is {stage}")
            return 403, {"message": "It is not your turn or you don't have an ability!", "error": "It is not your turn"}
        else:
            # todo: call abilities functions
            pass
    except Exception as e:
        return 500, {"message": "Error setting player!", "error": e}
