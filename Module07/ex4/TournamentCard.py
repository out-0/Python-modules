from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
from typing import Dict


class TournamentCard(Card, Combatable, Rankable):
    """
    Card with a high useful abilities included
    capability to enter tournaments matches
    """

    def __init__(self,
                 card_id: str,
                 name: str,
                 cost: int,
                 rarity: str,
                 attack: int,
                 defense: int,
                 health: int
                 ) -> None:
        """Initialize a base state of creature card"""
        super().__init__(name, cost, rarity)
        self.attack_value: int = attack
        self.health_value: int = health
        self.defense_value: int = defense
        self.card_id: str = card_id
        self.health_for_rating: int = self.health_value

        # Rating stuff -----------
        self.wins: int = 0
        self.losses: int = 0
        self.total_matches: int = 0

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

        return {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': 'Creature summoned to battlefield'
                }

    def attack(self, target) -> dict:
        """
        Attack target and damage it after let it defend itself.

        Validates that attack and health are positive integers

        Check phases:

        1:
        # Check if the attack and health is negative
        # which mean that card can't attack or Card
        # already dead.

        2:
        # Check if the target actually can be attacked,
        # of course if its not a Tournament (monster, elf...)
        # we cant attack another type like Spell Card.
        # if error raised while accessing those attribute its mean
        # the Card doesn't have them.
        """

        # Phase 1 check.
        if self.health_value <= 0:
            return {"Error": "already Dead 💀 "}
        if self.attack_value < 0:
            return {"Error": "Warring: Invalid Card Attack value"}

        # Phase 2 check
        if isinstance(target, TournamentCard):
            # Attack the target
            # Let the defend control the damage
            defense_result: Dict = target.defend(self.attack_value)
            damage_dealt: int = defense_result['damage_taken']

        else:
            return {"Error": ("Not TournamentCard, you can't attack it 💥 ")}

        # Fill the battle information
        # The Creature Card(self) is attacking the target
        # and damage it.
        result: Dict = {
                        'attacker': self.name,
                        'target': target.name,
                        'damage_dealt': damage_dealt,
                        'combat_resolved': True
                        }
        return result

    def defend(self, incoming_damage: int) -> dict:
        """
        defend an incoming_damage.

        Validates that the card still alive and a valid incoming value.

        Check phases:
        1:
        # Check if the defender alive

        2:
        # Check for valid data

        If all good, do the calculation based on the defender
        to subtract the damage from its health and return
        correct stats of the defense.
        """

        if self.health_value <= 0:
            return {"Error": "already dead ☠️"}
        if incoming_damage is None or incoming_damage < 0:
            return {"Error": "Invalid incoming damage provided ❌️"}
        # Set defaults so they always exist
        damage_blocked = self.defense_value
        damage_taken = max(0, incoming_damage - damage_blocked)

        # Apply the damage
        self.health_value -= damage_taken

        return {
                'defender': self.name,
                'damage_taken': damage_taken,
                'damage_blocked': damage_blocked - damage_taken,
                }

    def get_combat_stats(self):
        """
        Return a snapshot of the stats
        of comabat interface
        """
        pass

    def calculate_rating(self) -> int:
        """
        Calculates rating based on base stats + tournament performance.
        Formula: 1000 + (Attack + HP) * 10 + (Wins - Losses) * 16
        """

        # Base power based on attack and health so they start from
        # a logical and dynamic rating
        # We use a base of 1000 so no card starts at 0
        base_power = 1000 + (self.attack_value + self.health_for_rating) * 10

        # Performance points (16 points per win or loss shift)
        # This matches the +16/-16 shift seen in the demo
        # That will be dynamically modified for several cards
        tournament_points = (self.wins - self.losses) * 16

        return base_power + tournament_points

    def get_tournament_stats(self) -> dict:
        """Getting tournament Card stats"""
        return {
                'card_id': self.card_id,
                'name': self.name,
                'rarity': self.rarity,
                'performance': {
                                'wins': self.wins,
                                'losses': self.losses,
                                'total_matches': self.total_matches,
                                },
                'rating': self.calculate_rating()
                }

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
