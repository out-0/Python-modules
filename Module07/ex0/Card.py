from abc import ABC, abstractmethod


class Card(ABC):
    """Abstract base class of Card that represent
    what essential card must have"""

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """Initialize a base stats for a Card
        - Card name
        - Card cost (Mana cost)
        - Card rarity
        """

        self.name: str = name
        self.cost: int = cost
        self.rarity: str = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """Abstract play method which must be overrided
        when inherited"""
        pass

    # Concrete method have a default implementation.
    def get_card_info(self) -> dict:
        """Return a default dictionary represent card
        info based on card initialized.

        return dictionary(card info)

        """

        return {
                'name': self.name,
                'cost': self.cost,
                'rarity': self.rarity,
                }

    # Concrete method have a default implementation.
    def is_playable(self, available_mana: int) -> bool:
        """Check if the cost of the available_mana can hold the card cost

        Argument = available mana
        return -> True(Is playable) or False(Not Playable)

        """

        # Check if the available_mana hold the cost of card.
        if self.cost > available_mana:
            return False
        return True
