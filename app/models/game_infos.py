from app.models.roles_enums import Gods, Villagers, FenceSitters, Werewolves

game_info_model = {
    "witch_kill": None,
    "witch_save": None,
    "last_guarded": None,
}

night_info_model = {
    "witch_kill": None,
    "witch_save": None,
    "ww_kill": None,
    "guarded": None
}

first_night_order = [FenceSitters.THIEF, FenceSitters.CUPID, FenceSitters.WILDCHILD]
every_night_order = [Werewolves.WEREWORLF, Gods.SEER, Gods.GUARD, Gods.WITCH, Gods.KNIGHT, Gods.HUNTER]
