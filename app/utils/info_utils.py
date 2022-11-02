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


def validate_roles(roles: list):
    if roles is None or len(roles) < 3:
        return False, "Number of roles smaller than 3."
    else:
        for role in roles:
            if(
                not Gods.has_value(role)
                and not Werewolves.has_value(role)
                and not FenceSitters.has_value(role)
                and not Villagers.has_value(role)
            ):
                return False, f"{role} contains typo or this role is not supported yet."
        return True, "roles are good!"
