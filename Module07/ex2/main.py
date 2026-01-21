from ex2.EliteCard import EliteCard
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex1.main import Rarity


def main() -> None:
    """"""

    print("\n=== DataDeck Ability System ===\n")

    # ----------A general function to get class methods.
    def get_all_public_methods(cls):
        """Get all public methods from a class (abstract AND concrete)
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

    # ---------------------------------------------------

    print("EliteCard capabilities:")

    # Get abstract methods from each interface
    card_methods = get_all_public_methods(Card)
    combatable_methods = get_all_public_methods(Combatable)
    magical_methods = get_all_public_methods(Magical)
    print(f"- Card: {card_methods}")
    print(f"- Combatable: {combatable_methods}")
    print(f"- Magical: {magical_methods}")

    # Create Arcane Warrior (Elite Card)
    arcane_warrior: EliteCard = EliteCard("Arcane Warrior", 15,
                                          Rarity.LEGENDARY.value, 20, 18)

    # ----------Playing Arcane Warrior Elite Card----------

    battlefield: List = []
    game_state: dict = {'is_playable': arcane_warrior.is_playable(),
                        'available_mana': available_mana,
                        'battlefield': battlefield}
    playing_result: Dict = arcane_warrior.play()
    card_name: str = pass
    card_type: str = pass
    print("Playing Arcane Warrior ({}):")


main()
