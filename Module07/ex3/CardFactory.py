from abc import ABC, abstractmethod
from ex0.Card import Card


class CardFactory(ABC):
    """
    Interface for factories who responsible to create
    their categories of cards
    """

    @abstractmethod
    def create_creature(self, name_or_power) -> Card:
        """
        Helpful method to create those base
        Creature cards who can fight in battlefield
        """
        pass

    @abstractmethod
    def create_spell(self, name_or_power) -> Card:
        """
        Helpful method to create those base
        Spell cards who can be spelled.
        """
        pass

    @abstractmethod
    def create_artifact(self, name_or_power) -> Card:
        """
        Helpful method to create those base
        Artifact cards who can be used.
        """
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        """
        Create a collection of deck cards
        based on the size
        """
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        """
        Return the supported categories of cards
        """
        pass
