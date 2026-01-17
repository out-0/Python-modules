from . import elements


def healing_potion() -> str:
    """healing potion"""

    fire_result: str = elements.create_fire()
    water_result: str = elements.create_water()
    return f"Healing potion brewed with {fire_result} and {water_result}"


def strength_potion() -> str:
    """Increase the strength"""

    earth_result: str = elements.create_earth()
    fire_result: str = elements.create_fire()
    return f"Strength potion brewed with {earth_result} and {fire_result}"


def invisibility_potion() -> str:
    """Make the player invisible for a little time."""

    water_result: str = elements.create_water()
    air_result: str = elements.create_air()
    return f"Invisibility potion brewed with {air_result()} and {water_result}"


def wisdom_potion() -> str:
    """Increase intelligent"""

    all_four_result: str = "\n"
    all_four_result += elements.create_fire() + "\n"
    all_four_result += elements.create_water() + "\n"
    all_four_result += elements.create_earth() + "\n"
    all_four_result += elements.create_air()

    return f"Wisdom potion brewed with all elements: {all_four_result}"
