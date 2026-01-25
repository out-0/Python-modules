from ex2.EliteCard import EliteCard
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex1.main import Rarity
from typing import List, Dict
from ex0.CreatureCard import CreatureCard


# ----------A general function to get class methods.
def get_all_public_methods(cls):
    """
    Get all public methods from a class (abstract AND concrete)
    Since the Card class has methods that not abstract so we can't
    just do .__abstractmethods__, so for that we get all class
    public methods by filtering them to avoid the classes start with
    (" _ ") which is builtin.

    from class return the method or attribute match the name.
    getattr(cls, method_name)

    you can add callable() to be sure its a method
    """

    # List comprehension
    return [name for name in dir(cls)
            if not name.startswith('_') and callable(getattr(cls, name))]


def main() -> None:
    """Main entry point"""

    # The battlefield where the creatures fight
    battlefield: List[Card] = []

    print("\n=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")

    # Get abstract methods from each interface
    card_methods = get_all_public_methods(Card)
    combatable_methods = get_all_public_methods(Combatable)
    magical_methods = get_all_public_methods(Magical)
    print(f"- Card: {card_methods}")
    print(f"- Combatable: {combatable_methods}")
    print(f"- Magical: {magical_methods}")

    # Create Arcane Warrior (Elite Card)
    arcane_warrior: EliteCard = EliteCard("Arcane Warrior", 10,
                                          Rarity.LEGENDARY.value, 5, 5, 15)

    # Create enemy to be attacked(Creature Card)
    enemy: EliteCard = EliteCard("Enemy", 7,
                                 Rarity.RARE.value, 7, 0, 10)

    # ----------Playing Arcane Warrior Elite Card----------
    print(f"\nPlaying {arcane_warrior.name} "
          f"({arcane_warrior.__class__.__name__}):")

    player1_available_mana: int = 20
    is_playable: bool = arcane_warrior.is_playable(player1_available_mana)
    game_state: dict = {
            'is_playable': is_playable,
            'available_mana': player1_available_mana,
            'battlefield': battlefield
            }
    arcane_warrior.play(game_state)  # No need of returned here

    # ----------Playing Enemy card without printing the result----------
    player2_available_mana: int = 15
    is_playable: bool = enemy.is_playable(player2_available_mana)
    game_state: dict = {
            'is_playable': is_playable,
            'available_mana': player2_available_mana,
            'battlefield': battlefield
            }
    enemy.play(game_state)  # No need of returned here

    # ----------Start battle (arcane_warrior VS enemy)
    #
    # ##########Combat phase:
    print("\nCombat phase:")

    attack_result: Dict = arcane_warrior.attack(enemy)
    print(f"Attack result: {attack_result}")

    defense_result: Dict = arcane_warrior.defend(enemy.attack_power)
    print(f"Defense result: {defense_result}")

    # ##########Magic phase
    print("\nMagic phase:")

    # Create 2 enemies, this time lets make them just normal Creature.
    enemy1: CreatureCard = CreatureCard("Enemy1", 4,
                                        Rarity.COMMON.value, 2, 2)
    enemy2: CreatureCard = CreatureCard("Enemy2", 3,
                                        Rarity.RARE.value, 3, 3)

    targets: List[Card] = [enemy1.name,
                           enemy2.name]

    spell_result: Dict = arcane_warrior.cast_spell("Fireball", targets)
    print(f"Spell cast: {spell_result}")

    print(f"Mana channel: {arcane_warrior.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")


main()
