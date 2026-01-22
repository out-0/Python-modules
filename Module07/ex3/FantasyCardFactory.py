from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.main import Rarity
from ex1.ArtifactCard import ArtifactCard
from typing import Dict, List


# ===== CREATURES =====
class Dragon(CreatureCard):
    def __init__(self):
        super().__init__("Fire Dragon", 5, Rarity.LEGENDARY.value, 7, 5)


class Goblin(CreatureCard):
    def __init__(self):
        super().__init__("Goblin Warrior", 2, Rarity.COMMON.value, 2, 2)


# ===== SPELLS =====
class Fire(SpellCard):
    def __init__(self):
        super().__init__("Fireball", 3, Rarity.COMMON.value, "Deal 4 damage")


class Ice(SpellCard):
    def __init__(self):
        super().__init__("Ice Lance", 2, Rarity.COMMON.value, "Freeze target")


class Lightning(SpellCard):
    def __init__(self):
        super().__init__("Lightning Bolt", 3, Rarity.RARE.value,
                         "Deal 3 damage")


# ===== ARTIFACTS =====
class Rings(ArtifactCard):
    def __init__(self):
        super().__init__("Mana Ring", 1, Rarity.UNCOMMON.value, 5, "+1 mana per turn")


class Staffs(ArtifactCard):
    def __init__(self):
        super().__init__("Magic Staff", 3, Rarity.RARE.value, 3, "Boost spell damage")


class Crystals(ArtifactCard):
    def __init__(self):
        super().__init__("Power Crystal", 2, Rarity.UNCOMMON.value, 4, "Draw extra card")


class FantasyCardFactory(CardFactory):
    """
    Card Catalog that has a several Cards representation and ready
    to build the card anytime, its just to need which type of card
    to create.

    """

    def __init__(self):
        """
        Initialize an extensible card type registration
        which kinda like organized way to support the appending later,
        in our case e using dictionaries that can appended easy later.
        """

        self._creature_types: Dict = {
                                     "dragon": Dragon,
                                     "goblin": Goblin
                                     }

        self._spell_types: Dict = {
                                  "fireball": Fire,
                                  "ice": Ice,
                                  "Lightning": Lightning
                                  }

        self._artifact_types: Dict = {"mana_ring": Rings}

    def create_creature(self, name_or_power) -> Card:
        """
        Create an creature card, based on the type provided,
        but the type must be in the catalog of types above
        (dragon, goblin)

        Take name or power:

        If a name is provided -> check which card type and return card from it.
        If power is provided -> check and return the type match the power.

        """

        # Current catalog of creature cards.
        creature_types: List[str] = ["dragon", "goblin"]

        if isinstance(name_or_power, str):
            card_type: str = name_or_power
            if card_type in creature_types:
                card_class: Card = self._creature_types[card_type]
                return card_class()
        elif isinstance(name_or_power, int):
            if name_or_power >= 7:
                return Dragon()
            elif name_or_power >= 2:
                return Goblin()
            else:
                print("Warring: be more precise in your choose.")
                return None
        else:
            print("Error: Invalid data, check again.")
            return None

    def create_spell(self, name_or_power) -> Card:
        """"""

        self.name: str = name_or_power

    def create_artifact(self, name_or_power) -> Card:
        """"""

        self.name: str = name_or_power

    def create_themed_deck(self, size: int) -> dict:
        """"""

        pass

    def get_supported_types(self) -> dict:
        """"""
        pass

