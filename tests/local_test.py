import random
import copy
from app.utils.log_utils import logger
from app.utils.game_utils import invoke
from app.models.roles_enums import Alignment, Gods, Werewolves, Villagers, FenceSitters
import app.services.game_info as gi
import app.services.game as game

logger.debug("Debug test started")

roles = [
    Villagers.VILLAGER,
    Villagers.VILLAGER,
    Villagers.VILLAGER,

    Gods.SEER,
    "witch",
    # Gods.HUNTER,

    FenceSitters.THIEF,

    Werewolves.WEREWORLF,
    Werewolves.WEREWORLF,
    Werewolves.WEREWORLF
]


def set_test_players():
    base_ip = '192.168.0.'
    count = 0
    global roles
    for i in range(1, len(roles)):
        game.set_player(i, base_ip+str(i))


# (status, msg) = game.setup_game(roles)
# set_test_players()
# gi.debug_print()
