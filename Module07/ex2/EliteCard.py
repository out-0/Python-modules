from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typeing import Dict


class EliteCard(Card, Combatable, Magical):
    """Super Power card type, that should have
    all the ability from its parent, and implement
    its behavior for all the interfaces."""

    def __init__(self, name, cost, rarity, attack, health):
        """Initialize the Elite Card after getting the base attributes from
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
        self.health: int = health
        self.attack: int = attack

    def play(self, game_state: dict) -> dict:
        """Specify the play method for Elite Card

        - Check the game state:
          if the Card is playable,
          if available mana can hold cost of Card,

        If all good: Add the Creature Card to the battlefield
        and return play result.

        """

        try:
            if not game_state['is_playable']:
                print("This Card is not playable ❌️, often bot enough mana.")
                return {}

            if game_state['available_mana'] < self.cost:
                print("MANA: too low mana, check playable state again❕️")
                return {}

        except Exception:
            print("Error Detected 💣️: game state access fail.")
            return {}

        # If all good:
        game_state['available_mana'] -= self.cost
        game_state['battlefield'].append(self.name)

        return {'card_played': self.name,
                'mana_used': self.cost,
                'effect': 'Super Elite summoned to battlefield'}

    def attack(self, target):
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
        if self.attack <= 0 and self.health <= 0:
            print("Your Elite Card is already Dead 💀")
            return {}
        # Phase 2 check.
        try:
            # Check target also has attack and health (Creature Card)
            if target.attack and target.health:
                pass
        except Exception:
            print("Target not a Elite Card, you can't attack it 💥")

        # Fill the battle information
        # The Creature Card(self) is attacking the target
        # and damage it.
        result: Dict = {'attacker': self.name,
                        'target': target.name,
                        'damage_dealt': self.attack,
                        'combat_resolved': True}
        return result

    def defend(self, incoming_damage: int):
        """"""
        pass

    def get_combat_stats(self):
        """"""
        pass



    def cast_spell(self, spell_name: str, targets: list):
        """"""

        pass



    def channel_mana(self, amount: int):
        """"""

        pass


    def get_magic_stats(self):
        """"""
        pass



print(EliteCard.mro())
