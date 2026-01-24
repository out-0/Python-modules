from ex4.TournamentCard import TournamentCard
from ex1.main import Rarity
from typing import List, Dict
from ex0.Card import Card


def main() -> None:
    """Main Entry point that demonstrate the management"""

    print("\n=== DataDeck Tournament Platform ===\n")

    print("Registering Tournament Cards...")

    fire_dragon: Card = TournamentCard(
                                       "dragon_001",
                                       "Fire Dragon", 8,
                                       Rarity.LEGENDARY.value, 10, 10
                                      )

    ice_wizard: Card = TournamentCard(
                                      "wizard_001",
                                      "Ice Wizard", 5,
                                      Rarity.RARE.value, 5, 10
                                     )

    platform: TournamentCard = TournamentCard()

    # Registering Cards in the Tournament
    platform.register(fire_dragon)
    platform.register(ice_wizard)

    # Extract the interfaces of object, (bases)
    bases: List = [obj.__name__ for obj in fire_dragon.__class__.__bases__]
    # Format the list as string to remove 'name' to match demo.
    # join = concatenate strings and separate them by ', '
    interfaces: str = ', '.join(bases)
    rank_info: Dict = fire_dragon.get_rank_info()

    print(f"{fire_dragon.name} (ID: {fire_dragon.card_id}):")
    print(f"- Interfaces: [{interfaces}]")
    print(f"- Rating: {rank_info['rating']}")
    print(f"- Record: {rank_info['record']}")

    print('')

    # Extract the interfaces of object, (bases)
    bases: List = [obj.__name__ for obj in ice_wizard.__class__.__bases__]
    # Format the list as string to remove 'name' to match demo.
    # join = concatenate strings and separate them by ', '
    interfaces: str = ', '.join(bases)
    rank_info: Dict = ice_wizard.get_rank_info()
    print(f"{ice_wizard.name} (ID: {ice_wizard.card_id}):")
    print(f"- Interfaces: [{interfaces}]")
    print(f"- Rating: {rank_info['rating']}")
    print(f"- Record: {rank_info['record']}")

    print('')

    # Creating a match between those two cards (fire dragon and ice wizard)
    print("Creating tournament match..")




    battlefield: List = []
    player1_mana: int = 30
    player2_mana: int = 30
    is_playable: bool = False

    game_state: Dict = {
                        'is_playable': is_playable,
                        'battlefield': battlefield,
                        'available_mana': None
                        }

    # List of kinda players map their mana and cards to play
    players = [
               {"mana": player1_mana, "card": fire_dragon},
               {"mana": player2_mana, "card": ice_wizard}
              ]

    for player in players:
        current_mana = player["mana"]
        current_card = player["card"]

        # Update the state first
        game_state['available_mana'] = current_mana

        # Now pass the actual dictionary, not the result of an update() call
        result = current_card.play(game_state)





main()
