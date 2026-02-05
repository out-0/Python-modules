from typing import Optional, List, Any, Tuple, Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Constructor that build function that combine two other
    functions with both arguments passed to them

    Arguments:
        - Two spell functions which is callable
    Return:
        - Function resulted from combine the two passed functions

    """

    # Check data not None
    if spell1 is None or spell2 is None:
        print("Error: Invalid data provided")
        return None

    # Check invalid data (callable arguments)
    if not callable(spell1) or not callable(spell2):
        print("Error: Your data not callable")
        return None

    # Create a function that take a unknown number of
    # positional or keyword arguments and return
    # tuple result of both functions processing values.
    def combine(*args: Any, **kwargs: Any) -> Tuple:
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


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """
    Create an amplified version of a spell.

    Returns a new callable that executes the base spell and
    multiplies its numeric return value by the given multiplier.

    Arguments:
        base_spell: A callable that returns a numeric value.
        multiplier: A positive integer used to scale the spell result.

    Returns:
        A callable that returns the amplified result.
    """

    # Check Invalid data
    if not base_spell or not multiplier:
        print("Error: Invalid data provided")
        return None
    if not callable(base_spell) or multiplier <= 0:
        print("Error: Value of your data is invalid")
        return None

    # Multiply the returned value from base_spell function
    # by the multiplier and return result.
    def amplifier() -> int:
        """
        Execute the base spell and amplify its result.

        Returns:
            The numeric result of the base spell multiplied
            by the multiplier.
        """
        base_spell_value: int = base_spell()
        return base_spell_value * multiplier

    return amplifier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """
    Create a conditional spell caster.

    Returns a new callable that executes the spell only if
    the condition evaluates to True using the same arguments.

    Arguments:
        condition: A callable returning a boolean value.
        spell: A callable to be executed if the condition succeeds.

    Returns:
        A callable that conditionally executes the spell.
    """

    def caster(*args: Any, **kwargs: Any) -> Optional[str]:
        """
        Conditionally execute a spell based on a predicate.

        Arguments:
            *args: Positional arguments passed to both condition and spell.
            **kwargs: Keyword arguments passed to both condition and spell.

        Returns:
            None if the spell is cast successfully,
            or the string "Spell fizzled" if the condition fails.
        """
        if condition(*args, **kwargs):
            spell(*args, **kwargs)
        else:
            return "Spell fizzled"

        return None

    # Return the function (caster)
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    """
    Create a sequence of spells executed in order.

    Returns a callable that executes all provided spells
    with the same arguments and collects their results.

    Arguments:
        spells: A list of callable spell functions.

    Returns:
        A callable that returns a list of spell results.
    """

    def speller(*args: Any, **kwargs: Any) -> List[Any]:
        """
        Execute all spells in sequence.

        Arguments:
            *args: Positional arguments passed to each spell.
            **kwargs: Keyword arguments passed to each spell.

        Returns:
            A list containing the result of each spell execution.
        """

        # List to hold the return of each spell
        spells_result: List[Any] = []

        for spell in spells:
            spells_result.append(spell(*args, **kwargs))

        return spells_result

    return speller


def main() -> None:
    """Main entry point"""

    # For spells, actually we can just use functions which
    # are callable by default, but just to demonstrate the concept
    # more, am creating a class and make the instance of it callable.

    # Callable object of fireball
    class Fireball:
        """Callable spell that represents a fire-based attack."""

        def __init__(self) -> None:
            """Initialize the fireball spell with its name."""

            self.name = "Fireball"

        def __call__(self, *args, **kwargs) -> str:
            """
            Cast the fireball spell on a target.

            Arguments:
                *args: Expected to contain the spell target.
            """

            return f"{self.name} hits {args[0]}"

    class Heals:
        """Callable spell that represents a healing action."""

        def __init__(self) -> None:
            """Initialize the healing spell with its name."""

            self.name = "Heals"

        def __call__(self, *args, **kwargs) -> str:
            """
            Cast the healing spell on a target.

            Arguments:
                *args: Expected to contain the spell target.

            Returns:
                A string describing the healing action.
            """

            return f"{self.name} {args[0]}"

    # List of targets to spell against
    test_targets: List[str] = ["Dragon", "Goblin", "Wizard", "Knight"]

    # Test spell combiner function
    print("Testing spell combiner...")
    combined_spell: Callable = spell_combiner(Fireball(), Heals())

    for target in test_targets:
        tuple_result: Tuple = combined_spell(target)
        print("Combined spell result: ")
        for t in tuple_result:
            print(t)
        print("")

    # Test power amplifier function
    print("Testing power amplifier...")

    test_values = [12, 5, 24]

    # Create a simple spell class
    class DarkLight:
        """Callable spell that returns a base numeric power value."""

        def __init__(self, base_value: int) -> None:
            """
            Initialize the spell with a base power value.

            Arguments:
                base_value: Numeric value returned by the spell.
            """
            self.base_value = base_value

        def __call__(self) -> int:
            """
            Execute the spell.

            Returns:
                The base power value.
            """
            return self.base_value

    # Create a amplifier function for each element and
    # print the base value to check that is doubled.
    for value in test_values:
        # Create instance from the class.
        base_spell: Callable = DarkLight(value)
        new_function: Callable = power_amplifier(base_spell, 2)
        print(f"Original: {base_spell()} Amplified: {new_function()}")


if __name__ == "__main__":
    main()
