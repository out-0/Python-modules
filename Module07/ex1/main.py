from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard, Card
from ex1.Deck import Deck
from enum import Enum
from typing import List, Type


# Main starting function.
def main() -> None:
    """Main entry point of script"""

    # ----------Create Cards types Enum
    class CardType(Enum):
        """Different cards type can be used during game"""

        CREATURE = CreatureCard
        SPELL = SpellCard
        ARTIFACT = ArtifactCard

    # ----------Enumerate rarity categories.
    class Rarity(Enum):
        """List a several rarity categories"""

        COMMON = "Common"
        RARE = "Rare"
        LEGENDARY = "Legendary"

    # ----------Demonstrate deck builder.
    print("\n=== DataDeck Deck Builder ===\n")

    print("Building deck with different card types...")

    # Create the Deck (the Cards manager 🔍️)
    deck: Deck = Deck()

    # ------------Create 3 different Cards type using there constant enum.

    # Spell card.
    lightning_bolt: SpellCard = CardType.SPELL.value("Lightning Bolt",
                                                     3,
                                                     Rarity.COMMON.value,
                                                     "Deal 3 damage to target")

    # Artifact card.
    mana_crystal: ArtifactCard = CardType.ARTIFACT.value(
                                "Mana Crystal",
                                2,
                                Rarity.RARE.value,
                                4,
                                "Permanent: +1 mana per turn")

    # Creature card
    fire_dragon: CreatureCard = CardType.CREATURE.value("Fire Dragon",
                                                        5,
                                                        Rarity.LEGENDARY.value,
                                                        7,
                                                        5)

    # ----------Add the cards created to the deck

    # list the current created cards and loop on them to add to deck.
    current_cards: List[Card] = [lightning_bolt, mana_crystal, fire_dragon]

    costs = 0
    for card in current_cards:
        deck.add_card(card)
        costs += card.cost

    # Print deck stats...
    print(f"Deck stats: {deck.get_deck_stats()}")

    # Start drawing card from deck and playing.
    # Since Deck has shuffle method so logically its
    # must shuffle before each draw since the draw is
    # must be randomly, but to match the assignment demo
    # we'll relay on the order of adding the cards to
    # deck so the draw will be ordered as the demo demonstrate
    # without using shuffle.
    print("\nDrawing and playing cards:\n")

    card_drawed: Card = deck.draw_card()
    card_name: str = card_drawed.name
    card_type: Type[Card] = type(card_drawed)
    print(f"Drew: {card_name} ({card_type})")
    print(f"Play result: {card_drawed.play()}")


main()
