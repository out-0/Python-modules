from ex0.CreatureCard import Card, CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from typing import List


class Deck:
    """Deck management system"""

    def __init__(self) -> None:
        """Initialize deck with a lists of cards

        all_cards = This hold all the cards can used later in draw
        creatures = The Creature Cards
        spells    = All Spell Cards
        artifact  = All Artifact Cards

        """
        self.all_cards: List[Card] = []
        self.creatures: List[CreatureCard] = []
        self.spells: List[SpellCard] = []
        self.artifacts: List[ArtifactCard] = []

    # Add Card to deck.
    def add_card(self, card: Card) -> None:
        """Take a card, check what type of it
        and add it to its specific list,
        also to the general list.
        """

        pass

    def remove_card(self, card_name: str) -> bool:
        """"""
        pass

    def shuffle(self) -> None:
        """Note for me, shuffle need to use random library"""
        pass

    def draw_card(self) -> Card:
        """"""
        pass

    def get_deck_stats(self) -> dict:
        """"""

        all_costs: float = 0.0
        for card in self.all_cards:
            all_costs += card.cost

        average: float = all_costs / len(self.all_cards)

        # round(3.333…) → 4 (nearest integer)
        # the second part is for after decimal places
        # round(number, after decimal)
        avg_cost: float = round(average, 1)

        return {'total_cards': len(self.all_cards),
                'creatures': len(self.creatures),
                'spells': len(self.spells),
                'artifacts': len(self.artifacts),
                'avg_cost': avg_cost}
