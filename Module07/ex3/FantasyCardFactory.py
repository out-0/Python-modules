from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.main import Rarity
from ex1.ArtifactCard import ArtifactCard
from typing import Dict, List
import random


# ---- CREATURES ----
class Dragon(CreatureCard):
    """"""
    def __init__(self):
        super().__init__("Fire Dragon", 5, Rarity.LEGENDARY.value, 7, 5)


class Goblin(CreatureCard):
    """"""
    def __init__(self):
        super().__init__("Goblin Warrior", 2, Rarity.COMMON.value, 2, 2)


# ---- SPELLS -----
class Fire(SpellCard):
    """"""
    def __init__(self):
        super().__init__("Fireball", 4, Rarity.COMMON.value, "Deal 4 damage")


class Ice(SpellCard):
    """"""
    def __init__(self):
        super().__init__("Ice Lance", 2, Rarity.COMMON.value, "Freeze target")


class Lightning(SpellCard):
    """"""
    def __init__(self):
        super().__init__("Lightning Bolt", 3, Rarity.RARE.value,
                         "Deal 3 damage")


# ---- ARTIFACTS -----
class Rings(ArtifactCard):
    """"""
    def __init__(self):
        super().__init__("Mana Ring", 1, Rarity.RARE.value, 5, "+1 mana per turn")

class Staffs(ArtifactCard):
    """"""
    def __init__(self):
        super().__init__("Magic Staff", 3, Rarity.EPIC.value, 3, "Boost spell damage")


class Crystals(ArtifactCard):
    """"""
    def __init__(self):
        super().__init__("Power Crystal", 2, Rarity.RARE.value, 4, "Draw extra card")


# - Fantasy factory
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
                                  #"ice": Ice,
                                  #"lightning": Lightning
                                  }

        self._artifact_types: Dict = {"mana_ring": Rings}

    def create_creature(self, name_or_power) -> Card:
        """
        Create an creature card, based on the category name provided,
        but the type must be in the catalog of types above
        (dragon, goblin)

        Take name or power:

        If a name is provided -> check which card type and return card from it.
        If power is provided -> check and return the type match the power.

        """

        # Current catalog of creature cards.
        creature_categories: List[str] = ["dragon", "goblin"]

        # Handle string (name)
        if isinstance(name_or_power, str):
            card_name: str = name_or_power
            if card_name in creature_categories:
                card_class = self._creature_types[card_name]
                return card_class()
        # Handle power (int)
        elif isinstance(name_or_power, int):
            if name_or_power >= 7:
                return Dragon()
            elif name_or_power >= 2:
                return Goblin()
            else:
                print("Warring: be more precise in your choose.")
            
        print("Error: Invalid data, check again ❌️ ")
        print("Or just take that shit goblin hehe 👺 ")
        return Goblin()

    def create_spell(self, name_or_power) -> Card:
        """
        Create an Spell card, based on the type category name,
        provided but the type must be in the catalog of types above
        (Fireball, Ice Lance, Lightning Bolt)

        Take name or power:

        If a name is provided -> check which card category and return card from it.
        If power is provided -> check and return the type match the power.

        """

        # Current catalog of creature cards.
        spell_categories: List[str] = ["Fireball", "Ice Lance", "Lightning Bolt"]

        # Handle string (name)
        if isinstance(name_or_power, str):
            card_name: str = name_or_power
            if card_name in spell_categories:
                card_class = self._spell_types[card_name]
                return card_class()
        
        # Handle power (int)
        elif isinstance(name_or_power, int):
            if name_or_power >= 4:
                return Fire()
            elif name_or_power >= 3:
                return Lightning()
            elif name_or_power <= 2:
                return Ice()
            else:
                print("Warring: be more precise in your choose.")
                print("Also: because your mistake so take that shit ice lance 🧊 ")
                return Ice()
            
        print("Error: Invalid data, check again ❌️ ")
        print("Or just take that shit ice lance hehe 🧊")
        return Ice()

    def create_artifact(self, name_or_power) -> Card:
        """
        Create an Artifact card, based on the type category name,
        provided but the type must be in the catalog of types above
        (Mana Ring, Magic Staff, Power Crystal)

        Take name or power:

        If a name is provided -> check which card category and return card from it.
        If power is provided -> check and return the type match the power.

        """

        # Current catalog of creature cards.
        artifact_categories: List[str] = ["Mana Ring", "Magic Staff", "Power Crystal"]

        # Handle string (name)
        if isinstance(name_or_power, str):
            card_name: str = name_or_power
            if card_name in artifact_categories:
                card_class = self._spell_types[card_name]
                return card_class()
        # Handle power (int)
        elif isinstance(name_or_power, int):
            if name_or_power >= 3:
                return Staffs()
            elif name_or_power == 2:
                return Crystals()
            elif name_or_power == 1:
                return Rings()
            else:
                print("Warring: be more precise in your choose.")
                print("Also: because its your mistake so take that shit ring 💍 ")
                return Rings()
            
        print("Error: Invalid data, check again ❌️ ")
        print("Or just take that shit ring hehe 💍 ")
        return Rings()

    def create_themed_deck(self, size: int) -> dict:
        """
        Create themed deck, which is a collection of supported
        cards, based on the size provided (size)
        """

        # Result dict map the cards categories which types
        result: Dict = {
                       "creatures": [],
                       "spells": [],
                       "artifacts": [],
                       "total count": 0
                       }

        # Get dictionary of supported types
        supported_types: Dict = self.get_supported_types()

        # Extract list of categories from the supported types.
        all_types: List = (
                          supported_types['Creatures'] +
                          supported_types['spells'] +
                          supported_types['artifacts']
                          )

        # Get a random category each time and create card for it
        # and list it in the type list.
        for _ in range(size):
            chosen_card: Card = random.choice(all_types)

            if chosen_card in self._creature_types:
                card = self.create_creature(chosen_card)
                result['creatures'].append(card)

            elif chosen_card in self._spell_types:
                card = self.create_spell(chosen_card)
                result['spells'].append(card)

            elif chosen_card in self._artifact_types:
                card = self.create_artifact(chosen_card)
                result['artifacts'].append(card)

            else:
                print("Error: something happen while creating themed deck")
                return {}

        result['total count'] = size
        return result


    def get_supported_types(self) -> dict:
        """Return a structural of types available

        Taking the types registered in the initializing
        and return them organized.
        """
        return {
            'creatures': list(self._creature_types.keys()),
            'spells': list(self._spell_types.keys()),
            'artifacts': list(self._artifact_types.keys())
        }

