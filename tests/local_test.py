from app.utils.loggers import logger
from app.models.roles_enums import Alignment, Gods, Werewolves, Villagers, FenceSitters
import app.services.game_info as gi
from app.services.game import setup_game

logger.debug("Debug test started")

roles = [
    Villagers.VILLAGER,
    Villagers.VILLAGER,
    Villagers.VILLAGER,

    Gods.SEER,
    Gods.WITCH,
    Gods.HUNTER,

    Werewolves.WEREWORLF,
    Werewolves.WEREWORLF,
    Werewolves.WEREWORLF
]


def set_test_players():
    base_ip = '192.168.0.'
    count = 0
    global roles
    for i in range(1, len(roles)):
        gi.set_player(i, base_ip+str(i))


# (status, msg) = setup_game(roles)
# set_test_players()
gi.debug_print()
