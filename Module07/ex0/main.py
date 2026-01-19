from ex0.CreatureCard import CreatureCard
from typing import Dict, List
from enum import Enum


def main() -> None:
    """Main starting point to run"""

    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    # Demonstrate the enumeration by a simple rarity category.
    class Rarity(Enum):
        """List the rarity categories"""

        COMMON = "Common"
        RARE = "Rare"
        LEGENDARY = "Legendary"

    # Create dragon which a Creature card[Name, cost, rarity, attack, health]
    fire_dragon: CreatureCard = CreatureCard("Fire Dragon",
                                             5,
                                             Rarity.LEGENDARY.value,
                                             7,
                                             5)

    print("CreatureCard Info:")
    print(fire_dragon.get_card_info())

    available_mana: int = 6
    print(f"\nPlaying Fire Dragon with {available_mana} mana available:")

    # Check if that Card can be played which the current available_mana.
    is_playable: bool = fire_dragon.is_playable(available_mana)
    print(f"Playable: {is_playable}")

    # A battlefield list that hold all the Hero's or Creatures in game.
    battlefield: List = []

    # Pass the current game state and print the returned
    # result of playing this Card.
    play_dragon: Dict = fire_dragon.play({'is playable': is_playable,
                                          'available mana': available_mana,
                                          'battlefield': battlefield})
    print(f"Play result: {play_dragon}")

    # First, Creating the goblin warrior.
    goblin_warrior: CreatureCard = CreatureCard("Goblin Warrior",
                                                2,
                                                Rarity.COMMON.value,
                                                3,
                                                2)

    # Try attacking a goblin.
    print("\nFire Dragon attacks Goblin Warrior:")
    attack_result: Dict = fire_dragon.attack_target(goblin_warrior)
    print(f"Attack result: {attack_result}")

    # Try an insufficient mana, which can't summon a CreatureCard like
    # fire dragon who cost 5 mana.
    available_mana: int = 3
    print(f"\nTesting insufficient mana ({available_mana} available):")
    is_playable: bool = fire_dragon.is_playable(available_mana)
    print(f"Playable: {is_playable}")

    print("\nAbstract pattern successfully demonstrated!")


main()
