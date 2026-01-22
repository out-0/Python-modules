from ex0.Card import Card
from ex3.FantasyCardFactory import Dragon, Lightning, Lightning, Goblin
from ex3.CardFactory import CardFactory
from typing import List


class GameEngine:
    """"""

    def __init__(self):
        """"""
        

    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        """"""
        self.factory: CardFactory = factory
        self.strategy = strategy
        print(f"Configuring {factory.__class__.__name__} "
              f"with {strategy.get_strategy_name()}...")

    def simulate_turn(self) -> dict:
        """Simulate a turn of an strategy cards
        which is just make the cards for the strategy
        and provide them an organized way.
        """

        # Create 3 random cards dynamically
        # ->>> deck_cards = self.factory.create_themed_deck(3)

        # In real game at least we'll use the above line
        # but to match the demo we'll just static those cards.
        Cards_for_demo: List[Card] = [Dragon(), Goblin(), Lightning()]

        # Build structured list represent name (cost)
        fucking_structured_list: List = []
        for card in Cards_for_demo:
            name = card.name
            cost = card.cost
            fucking_structured_list.append(f"{name} ({cost})")
       

        return {"Hand": fucking_structured_list}

    def get_engine_status(self) -> dict:
        """"""
        pass
