from ex0.Card import Card


class CreatureCard(Card):
    """Creature card representation which is a card of a creature can attack
    defense, and have a several effects.
    """

    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 attack: int,
                 health: int
                 ) -> None:
        """Initialize the creature card after getting the base attributes from
        the base Card, and then add some functional attributes.

        Base stats:
            - Name
            - Cost
            - Rarity

        Stats added:
            - Attack
            - Health

        Specific added: [since the class know the type of itself lets set it]
            - Type

        """

        super().__init__(name, cost, rarity)
        self.attack: int = attack
        self.health: int = health
        self.type: str = "Creature"

    # Implements the abstract play method
    def play(self, game_state: dict) -> dict:
        """Specify the play method for Creature card"""


        return {'card_played': self.name,
                'mana_used': self.cost,
                'effect': 'Creature summoned to battlefield'}

    def attack_target(self, target) -> dict:
        """Attack a specific target and damage it.

        Validates that attack and health are positive integers
        """
        pass
