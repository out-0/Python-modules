from typing import List
from ex0.Card import Card

class AggressiveStrategy:
    """This strategy is relay on using the cards that cost
    less than 5 mana point.
    """

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Execute the hand with that strategy used.
        
        Argument => Hand

        Check all the hand and play the card just if it cost
        less than 5 mana

        Return report of the actions used

        """

        # Define the result info
        cards_played: List[Card] = []
        mana_used: int = 0
        damage_dealt: int = 0
        targets_attacked: List[Card] = []

        # Check the hand in fill the info
        for card in hand:
            if card.cost < 5:
                card.play()  # => Play card
                cards_played.append(card)  # => Add to played




    def get_strategy_name(self) -> str:
        """Just return the strategy name"""
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        pass


