from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """"""

    def __init__(self,
                 card_id: str,
                 name: str,
                 cost: int,
                 rarity: str,
                 attack: int,
                 health: int
                 ) -> None:
        """Initialize a base state of creature card"""
        super().__init__(name, cost, rarity)
        self.attack_value: int = attack
        self.health_value: int = health
        self.card_id: str = card_id

        # Rating stuff -----------
        self.wins: int = 0
        self.losses: int = 0

    def play(self, game_state: dict) -> dict:
        """Specify the play method for Creature Card

        - Check the game state:
          if available mana can hold cost of Card,

        If all good: Add the Creature Card to the battlefield
        and return play result.

        """

        try:
            if game_state['available_mana'] < self.cost:
                print("MANA: too low mana, check playable state again❕️")
                return {}

        except Exception:
            print("Error Detected 💣️: game state access fail.")
            return {}

        # If all good:
        game_state['available_mana'] -= self.cost
        game_state['battlefield'].append(self)

        return {'card_played': self.name,
                'mana_used': self.cost,
                'effect': 'Creature summoned to battlefield'}

    def attack(self, target) -> dict:
        """"""
        pass

    def defend(self, incoming_damage: int):
        """defend interface for other
        specialized Combatable types"""
        pass

    def get_combat_stats(self):
        """Return a snapshot of the stats
        of comabat interface"""
        pass

    def calculate_rating(self) -> int:
        """
        Calculates rating based on base stats + tournament performance.
        Formula: 1000 + (Atk + HP) * 10 + (Wins - Losses) * 16
        """

        # Base power based on attack and health so they start from
        # a logical and dynamic rating
        # We use a base of 1000 so no card starts at 0
        base_power = 1000 + (self.attack_value + self.health_value) * 10

        # Performance points (16 points per win or loss shift)
        # This matches the +16/-16 shift seen in the demo
        # That will be dynamically modified for several cards
        tournament_points = (self.wins - self.losses) * 16

        return base_power + tournament_points

    def get_tournament_stats(self) -> dict:
        """"""
        pass

    def update_wins(self, wins: int) -> None:
        """Just update the wins attribute"""
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        """Just update the losses attribute"""
        self.losses += losses

    def get_rank_info(self) -> dict:
        """Return representation of rank information"""
        return {
                "id": self.card_id,
                "name": self.name,
                "rating": self.calculate_rating(),
                "record": f"{self.wins}-{self.losses}"
            }
