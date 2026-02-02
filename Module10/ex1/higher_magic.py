from typing import Optional, List, Any, Dict, Tuple


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    """Constructor that build function that combine two other
    functions wiht both argumetns passed to them

    Arguments:
        - Two spell functions which is callable
    Return:
        - Function resulted from combine the two passed functions

    """

    # Check data not None
    if not spell1 or not spell2:
        print("Error: Invalid data provided")
        return None

    # Check invalid data (callable arguments)
    if not callable(spell1) or not callable(spell2):
        print("Error: Your data not callable")
        return None

    # Create a function that take a unknown number of
    # positional or keyword arguments and return
    # tuple result of both functions processing values.
    def combine(*args: tuple, **kwargs: dict) -> tuple:
        """Take arbitrary arguments that gonna passed to
        a two functions (spell1, spell2) and Return
        a tuple resulted from the return of the Two
        function.

        Arguments:
            - positional arguments, keyword arguments

        Return:
            - Tuple of values
        """

        value1 = spell1(*args, **kwargs)
        value2 = spell2(*args, **kwargs)

        return (value1, value2)

    # Return the function object itself.
    return combine


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    """"""

    # Check Invalid data
    if not base_spell or not multiplier:
        print("Error: Invalid data provided")
        return None
    if not callable(base_spell) or multiplier <= 0:
        print("Error: Value of your data is invalid")

    # Multiply the returned value from base_spell function
    # by the multiplier and return result.
    def amplifier() -> int:
        """"""
        base_spell_value: int = base_spell()
        return base_spell_value * multiplier

    return amplifier


def conditional_caster(condition: callable, spell: callable) -> callable:
    """"""

    def caster(*args: Tuple, **kwargs: Dict) -> Optional[str]:
        """"""
        if condition(*args, **kwargs):
            spell(args, kwargs)
        else:
            return "Spell fizzled"

        return None

    # Return the function (caster)
    return caster


def spell_sequence(spells: list[callable]) -> callable:
    """"""

    def speller(*args: tuple, **kwargs: Dict) -> List[Any]:
        """"""

        # List to hold the return of each spell
        spells_result: List[Any] = []

        for spell in spells:
            spells_result += spell(*args, **kwargs)

        return spells_result

    return speller


def main() -> None:
    """Main entry point"""


    # For spells, actually we can just use functions which
    # are callable by default, but just to demonstrate the concept
    # more, am creating a class and make the instance of it callable.
    
    # Callable object of fireball
    class Fireball:
        """"""
        def __init__(self):
            self.name = "Fireball"

        def __call__(self, *args, **kwargs):
            return f"{self.name} hits {args[0]}"

    class Heals:
        """"""
        def __init__(self):
            """"""
            self.name = "Heals"

        def __call__(self, *args, **kwargs):
            """"""
            return f"{self.name} {args[0]}"


    # List of targets to spell against
    test_targets: List[str] = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    print("Testing spell combiner...")
    combined_spell = spell_combiner(Fireball(), Heals())

    for target in test_targets:
        print(combined_spell(target))


main()

#Combined spell result: Fireball hits Dragon, Heals Dragon")
