from app.utils.loggers import logger
import app.services.game_info as gi


def setup_game(roles: list):
    try:
        gi.setup(roles)
    except Exception as e:
        logger.error("Error setting roles for the game!", e)
        logger.error(roles)
        return 500, {"message": "Cannot set roles for the game!", "error": e}

    gi.set_nbr_of_players(len(roles))
    return 200, {"message": f"game setup with roles: {str(roles)}"}
