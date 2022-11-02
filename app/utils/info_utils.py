from app.models.roles_enums import Gods, Werewolves, FenceSitters, Villagers


def validate_roles(roles: list):
    if roles is None or len(roles) < 3:
        return False, "Number of roles smaller than 3."
    else:
        for role in roles:
            if(
                not Gods.has_value(roles)
                and not Werewolves.has_value(roles)
                and not FenceSitters.has_value(roles)
                and not Villagers.has_value(roles)
            ):
                return False, f"{role} contains typo or this role is not supported yet."
        return True, "roles are good!"




