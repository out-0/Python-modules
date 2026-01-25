from ex0.Card import Card
from typing import Dict


# Creature Card who can summon to a battlefield.
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

        """

        super().__init__(name, cost, rarity)
        self.attack: int = attack
        self.health: int = health

    # Implements the abstract play method
    def play(self, game_state: dict) -> dict:
        """Specify the play method for Creature Card

        - Check the game state:
          if the Card is playable,
          if available mana can hold cost of Card,

        If all good: Add the Creature Card to the battlefield
        and return play result.

        """

        try:
            if not game_state['is_playable']:
                print("This Card is not playable ❌️, "
                      "often cause you don't have enough mana.")
                return {}

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

    # Return information of a card.
    def get_card_info(self) -> dict:
        """Return information about the Creature Card.

        return -> dict (dictionary of info)

        """

        # Get base info from parent.
        info: Dict = super().get_card_info()

        # Add specific info of Creature Card.
        info.update({
            'type': 'Creature',
            'attack': self.attack,
            'health': self.health
        })
        return info

    # Attack action for Creature Card.
    def attack_target(self, target) -> dict:
        """Attack a specific target and damage it.

        Validates that attack and health are positive integers

        Check phases:

        1:
        # Check if the attack and health is negative
        # which mean that card can't attack or Creature Card
        # already dead.

        2:
        # Check if the target actually can be attacked,
        # of course if its not a Creature Card(monster, elf...)
        # we cant attack another type like Spell Card.
        # if error raised while accessing those attribute its mean
        # the Card doesn't have them.


        """

        # Phase 1 check.
        if self.health <= 0:
            print("Your Creature Card is already Dead 💀")
            return {}
        if self.attack < 0:
            print("Warring: Invalid Card Attack value")
            return {}

        # Phase 2 check
        if isinstance(target, CreatureCard):
            # Damage the target
            target.health -= self.attack
        else:
            print("Target not a Creature Card, you can't attack it 💥")
            return {}

        # Fill the battle information
        # The Creature Card(self) is attacking the target
        # and damage it.
        result: Dict = {'attacker': self.name,
                        'target': target.name,
                        'damage_dealt': self.attack,
                        'combat_resolved': True}
        return result
