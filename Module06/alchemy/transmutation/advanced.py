from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    """Create philosophers stone"""

    lead_to_gold_result: str = lead_to_gold()
    healing_potion_result: str = healing_potion()
    return ("Philosopher’s stone created using "
            f"{lead_to_gold_result} and {healing_potion_result}")


def elixir_of_life() -> str:
    """Using Elixir of life"""

    return "Elixir of life: eternal youth achieved!"
