from app.models.roles_enums import Gods, FenceSitters, Werewolves

# todo: decide whether to use this or not
room_info_model = {
    "nbr_of_players": 0,
    "first_night_order": [],
    "every_night_order": []
}

game_info_model = {
    "roles": [],
    "players": [],
    "game_on_going": False,
    "game_start_datetime": None,
    "round": 0,
    "witch_kill": None,
    "witch_save": None,
    "hunter_status": True,
    "hunted": None,
    "lover_1": None,
    "lover_2": None,
    "last_guarded": None,
}

night_info_model = {
    "stage": -1,
    "witch_kill": None,
    "witch_save": None,
    "ww_kill": None,
    "silenced": None,
    "die_for_love": None,
    "guarded": None
}

public_night_info_model = {
    "dead": []
}

first_night_order_model = [FenceSitters.THIEF, FenceSitters.WILDCHILD, FenceSitters.CUPID]
every_night_order_model = [Werewolves.WEREWORLF, Gods.SEER, Gods.GUARD, Gods.WITCH, Gods.KNIGHT, Gods.HUNTER]
