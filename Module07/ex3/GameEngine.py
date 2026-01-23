from ex0.Card import Card
from ex3.FantasyCardFactory import Dragon, Lightning, Goblin, Enemy
from ex3.CardFactory import CardFactory
from typing import List, Dict
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """"""

    def __init__(self):
        """"""

    def configure_engine(self,
                         factory: CardFactory,
                         strategy: GameStrategy
                         ) -> None:
        """"""
        self.factory: CardFactory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        """Simulate a turn of an strategy cards
        which is just make the cards for the strategy
        and provide them an organized way.
        """

        # Create 3 random cards dynamically
        # ->>> Hand_cards = self.factory.create_themed_deck(3)

        # In real game at least we'll use the above line
        # but to match the demo we'll just static those cards.
        Cards_for_demo: List[Card] = [Dragon(), Goblin(), Lightning()]
        battlefield: List[Card] = [Enemy()]

        # Execute the turn based on the strategy specified.
        actions_result: Dict = self.strategy.execute_turn(
                                                          Cards_for_demo,
                                                          battlefield
                                                          )
        return actions_result

    def get_engine_status(self) -> dict:
        """"""
        pass
