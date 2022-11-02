from app.models.roles_enums import Alignment, Gods, Werewolves, FenceSitters, Villagers


def find_alignment(role: str) -> str:
    if Gods.has_value(role):
        return Alignment.GOD
    elif FenceSitters.has_value(role):
        return Alignment.IRRELEVANT
    elif Werewolves.has_value(role):
        return Alignment.WEREWOLF
    elif Villagers.has_value(role):
        return Alignment.VILLAGER
    else:
        return "role Error"
