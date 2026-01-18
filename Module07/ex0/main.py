from ex0.CreatureCard import CreatureCard
from typing import Dict, List
from enum import Enum

print('')
print("=== DataDeck Card Foundation ===")
print('')
print("Testing Abstract Base Class Design:")
print('')


# Define the Enum for a Fire Dragon and a Goblin Warrior
class FireDragon(Enum):
    NAME = "Fire Dragon"
    COST = 5
    RARITY = "Legendary"
    ATTACK = 7
    HEALTH = 5


class GoblinWarrior(Enum):
    NAME = "Goblin Warrior"
    COST = 2
    RARITY = "Common"
    ATTACK = 3
    HEALTH = 2


# Create the dragon which a Creature card[Name, cost, rarity, attack, health]
# pass the values of those Enum members as arguments.
fire_dragon: CreatureCard = CreatureCard(FireDragon.NAME.value,
                                         FireDragon.COST.value,
                                         FireDragon.RARITY.value,
                                         FireDragon.ATTACK.value,
                                         FireDragon.HEALTH.value)

print("CreatureCard Info:")
print(fire_dragon.get_card_info())

print('')
available_mana: int = 6
print(f"Playing Fire Dragon with {available_mana} mana available:")

# Check if that Card can be played which the current available_mana.
is_playable: bool = fire_dragon.is_playable(available_mana)
print(f"Playable: {is_playable}")


# A battlefield list that hold all the Hero's or Creatures in game.
battlefield: List = []

# Pass the current game state and print the returned
# result of playing this Card.
print(f"Play result: {fire_dragon.play({'is playable': is_playable,
                                        'available mana': available_mana,
                                        'battlefield': battlefield})}")

print('')
# First, Creating the goblin warrir.
goblin_warrior: CreatureCard = CreatureCard(GoblinWarrior.NAME.value,
                                            GoblinWarrior.COST.value,
                                            GoblinWarrior.RARITY.value,
                                            GoblinWarrior.ATTACK.value,
                                            GoblinWarrior.HEALTH.value)

# Try attacking a goblin.
print("Fire Dragon attacks Goblin Warrior:")
print(f"Attck result: {fire_dragon.attack_target(goblin_warrior)}")



