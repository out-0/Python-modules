from ex0.CreatureCard import Card, CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from typing import List, Dict, Type
import math
import random


class Deck:
    """Deck management system"""

    def __init__(self) -> None:
        """Initialize deck with a lists of cards

        All_cards = This hold all the cards can used later in draw
        creatures = The Creature Cards
        spells    = All Spell Cards
        artifact  = All Artifact Cards

        """
        self.all_cards: List[Card] = []
        self.creatures: List[CreatureCard] = []
        self.spells: List[SpellCard] = []
        self.artifacts: List[ArtifactCard] = []

        # Map Types class to their specific lists
        # Class of type -> Cards list
        # Type[Card] == the class of that specialized card.
        self._types_map: Dict[Type[Card], List] = {
            CreatureCard: self.creatures,
            SpellCard: self.spells,
            ArtifactCard: self.artifacts,
        }

    # Add Card to deck.
    def add_card(self, card: Card) -> None:
        """
        Take a card, check what type of it
        and add it to its specific list,
        also to the general list.
        """

        # Loop trough the types map and check which type the card
        # is and then add it to its specific list.
        for card_type, cards_list in self._types_map.items():
            if isinstance(card, card_type):
                cards_list.append(card)

        self.all_cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """
        Remove a specific card by its name

        Remove from deck all cards list, and
        from its specific card type list.

        """
        if card_name is None:
            print("Error: Data provided not valid 😤")
            return False

        for target_card in self.all_cards:
            if target_card.name == card_name:
                self.all_cards.remove(target_card)

                # Remove from specific list
                for card_type, cards_list in self._types_map.items():
                    if isinstance(target_card, card_type):
                        cards_list.remove(target_card)
                        return True
        # If not found
        print("Well, Card Not Found, Are you sure its in Deck ? 🔔")
        return False

    def shuffle(self) -> None:
        """Shuffle the current cards in Deck

        All_cards => shuffle (function) -> new random list.

        Argument of shuffle must = mutable iterable like list,
                                   not tuple not set.

        """
        if len(self.all_cards) == 0:
            print("Empty: Nothing to shuffle, deck empty 🎲")
        random.shuffle(self.all_cards)

    def draw_card(self) -> Card:
        """
        Drawing a card which mean remove it from the deck

        Its differ from remove, since drawing will draw the top
        card in deck which is kinda randomly if combined with
        shuffle.

        # Remove the last card object in the list,
        # and from the specialized type also return
        # the card as drawn card.

        If all good return drawn card.
        If error during search caught error and handle it.

        """

        try:
            # Remove and return last card object.
            drawn_card: Card = self.all_cards.pop()

            # Check that drawn card type to remove from its type list.
            for card_type, cards_list in self._types_map.items():
                if isinstance(drawn_card, card_type):
                    cards_list.remove(drawn_card)

        except IndexError:
            print("Error 💥: The Deck list is already empty")
        except ValueError:
            print("Error 💥: Card Not found in type list")

        return drawn_card

    def get_deck_stats(self) -> dict:
        """Return a dictionary that represent the current deck stats:

        - total cards count
        - creature cards count
        - spell cards count
        - artifact cards count
        - avg cost of all costs

        """

        # Generator for summing all the costs.
        all_costs: float = sum(card.cost for card in self.all_cards)

        average: float = 0.0
        try:
            average: float = all_costs / len(self.all_cards)
        except ZeroDivisionError:
            print("Error: Something wrong with your cards costs...‼️")
            print("Error: Some costs is 0‼️")

        # ceiling(3.333…) → 4 (nearest up integer)
        avg_cost: int = math.ceil(average)

        return {'total_cards': len(self.all_cards),
                'creatures': len(self.creatures),
                'spells': len(self.spells),
                'artifacts': len(self.artifacts),
                'avg_cost': float(avg_cost)}
