from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import Dict


class EliteCard(Card, Combatable, Magical):
    """Super Power card type, that should have
    all the ability from its parent, and implement
    its behavior for all the interfaces."""

    total_mana_channeled: int = 10

    def __init__(self, name, cost, rarity, attack, defense, health):
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
        self.attack_power: int = attack
        self.defense_power: int = defense

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
        game_state['battlefield'].append(self.name)

        return {'card_played': self.name,
                'mana_used': self.cost,
                'effect': 'Super Elite summoned to battlefield'}

    def attack(self, target) -> dict:
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
        if self.attack_power <= 0 and self.health <= 0:
            print("Your Elite Card is already Dead 💀")
            return {}
        # Phase 2 check.
        try:
            # Check target also has attack and health (Creature Card)
            if target.attack_power and target.health:
                pass
        except Exception:
            print("Error: Target "
                  "must be a creature card (monster, elf, human...) 💥")

        # ----------Calculate the damage applied.
        # Get value of defense attr if don't have assign default(0)
        target_defense: int = getattr(target, 'defense_power', 0)

        damage: int = self.attack_power - target_defense
        if damage < 0:
            damage: int = 0
        # Apply the damage to the target
        target.health -= damage
        if target.health <= 0:
            print(f"Agghhh: {target.name} dying 💀")
        # Fill the battle information
        result: Dict = {
                'attacker': self.name,
                'target': target.name,
                'damage': damage,
                'combat_type': 'melee'
                }
        return result

    def defend(self, incoming_damage: int) -> None:
        """defend an incoming_damage.

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

        if self.health <= 0:
            print("Dead: Your Card is already dead ☠️")
            return
        if incoming_damage is None or incoming_damage < 0:
            print("Error: Invalid incoming damage provided ❌️")
            return
        # Set defaults so they always exist
        damage_blocked = self.defense_power
        damage_taken = 0
        is_still_alive = self.health > 0
        try:
            damage_blocked: int = self.defense_power
            damage_taken: int = incoming_damage - damage_blocked
            self.health -= damage_taken
            is_still_alive: bool = self.health > 0

        except Exception:
            print("Error: something happen while defending 🛡️")

        return {
                'defender': self.name,
                'damage_taken': damage_taken,
                'damage_blocked': damage_blocked - damage_taken,
                'still_alive': is_still_alive
                }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """
        Casting the provided spell into a list of targets and damage them.

        Checks:

        - If no target provided -> return
        - If Card already dead -> return

        Since no available mana provided ill assume that the card
        have enough mana to cast the spell which cost 4 mana
        """

        if len(targets) == 0:
            print("Warring: No target specified ‼️")
            return {}
        if self.health <= 0:
            print("Warring: Your Card is already dead ☠️")
            return {}

        return {
                'caster': self.name,
                'spell': spell_name,
                'targets': targets,
                'mana_used': 4
                }

    def channel_mana(self, amount: int) -> dict:
        """A way or mechanism of recovering the energy which is mana
        channeled (recover mana) the amount requested and subtracted
        from the current mana pool value (total_mana_channeled)
        """
        if EliteCard.total_mana_channeled >= amount:
            EliteCard.total_mana_channeled -= amount
        else:
            print("Warring: The Pool of Mana is Empty 🔱 ")

        return {'channeled': amount,
                'total_mana': EliteCard.total_mana_channeled}

    def get_combat_stats(self) -> dict:
        """Returns a snapshot of the card's physical fighting capabilities."""
        return {
            'attack': self.attack_power,
            'defense': self.defense_power,
            'current_health': self.health,
            'combat_style': 'melee'
        }

    def get_magic_stats(self) -> dict:
        """Returns a snapshot of the card's magical energy and status."""
        return {
            'mana_pool': EliteCard.total_mana_channeled,
            'is_spellcaster': True,
            'can_cast_now': EliteCard.total_mana_channeled > 0
        }
