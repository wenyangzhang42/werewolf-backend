from app.models.roles_enums import Gods, Villagers, FenceSitters, Werewolves

game_info_model = {
    "round": 0,
    "witch_kill": None,
    "witch_save": None,
    "hunter_status": True,
    "hunted": None,
    "last_guarded": None,
}

night_info_model = {
    "stage": 0,
    "witch_kill": None,
    "witch_save": None,
    "ww_kill": None,
    "die_for_love": None,
    "guarded": None,
    "dead": []
}

first_night_order_model = [FenceSitters.THIEF, FenceSitters.CUPID, FenceSitters.WILDCHILD]
every_night_order_model = [Werewolves.WEREWORLF, Gods.SEER, Gods.GUARD, Gods.WITCH, Gods.KNIGHT, Gods.HUNTER]
