from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from typing import Dict
from ex3.FantasyCardFactory import Ice, Lightning
from ex3.GameEngine import GameEngine


def main() -> None:
    """"""

    print("\n=== DataDeck Game Engine ===\n")

    # ---------- Starting configuration ----------
    print('Configuring Fantasy Card Game...')

    fantasy_factory = FantasyCardFactory()
    print(f"Factory: {fantasy_factory.__class__.__name__}")

    aggressive_strategy = AggressiveStrategy()
    print(f"Strategy: {aggressive_strategy.get_strategy_name()}")

    # Print the supported types of cards matched demo
    supported_types: Dict = fantasy_factory.get_supported_types()
    print(f"Available types: {supported_types}")

    # Expend card type registration with new categories
    fantasy_factory._spell_types.update({
                                        "ice": Ice,
                                        "lightning": Lightning,
                                        })

    # Using the factory and strategy together in engine
    engine = GameEngine()
    engine.configure_engine(fantasy_factory, aggressive_strategy)

    # Show the hand cards will simulated.
    print("Simulating aggressive turn...")
    print("Hand: [Fire Dragon (5), Goblin Warrior (2), Lightning Bolt (3)]")


    print(engine.simulate_turn())







main()


