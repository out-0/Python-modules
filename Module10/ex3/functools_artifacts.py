from typing import Dict, Callable, List
import functools
import operator


# ----- reduce function from functools module -----
def spell_reducer(spells: list[int], operation: str) -> int:
    """
    Reduces a list of spell intensities into a single
    value using a specified operation.

    Args:
        spells: A list of integers representing spell power levels.
        operation: The arithmetic or logical operation to apply.
                   Supported: 'add', 'multiply', 'max', 'min'.

    Returns:
        The final reduced integer value.

    Raises:
        KeyError: If the operation provided is not in the supported map.
        TypeError: If the spells list is empty (reduce requires at least one).
    """

    # Map the supported operations to their callable fn.
    op_map: Dict[str, Callable] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }

    try:
        # Operate on the all spells items and return final value
        final_value: int = functools.reduce(op_map[operation], spells)
    except KeyError:
        print(f"Error: '{operation}' is not a supported spell operation.")
        return 0
    except TypeError:
        print("Error: Cannot reduce an empty spell list.")
        return 0

    return final_value


# ----- partial function from functools -----
def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """
    Creates specialized enchantment functions with pre-set attributes.

    This function uses partial application to fix the 'power' at 50 and
    assign specific 'element' types to the base enchantment logic.

    Args:
        base_enchantment: A function that accepts (power, element, target).

    Returns:
        A dictionary containing three partial functions:
        'fire_enchant', 'ice_enchant', and 'lightning_enchant'.
    """

    # functools.partial lets you take an existing function
    # and pre-fill some of its arguments so you get a new
    # simpler function that only needs the rest of the arguments later.
    fire_enchant: Callable = functools.partial(
        base_enchantment, power=50, element="fire"
    )
    ice_enchant: Callable = functools.partial(
        base_enchantment, power=50, element="ice"
    )
    lightning_enchant: Callable = functools.partial(
        base_enchantment, power=50, element="lightning"
    )

    return {
        "fire_enchant": fire_enchant,
        "ice_enchant": ice_enchant,
        "lightning_enchant": lightning_enchant,
    }


# ------ lru_cache decorator -----
@functools.lru_cache
def memoized_fibonacci(n: int) -> int:
    """
    Calculates the nth Fibonacci number using
    the LRU (Least-recently-used) cache for memoization.

    This function implements the Fibonacci sequence where each number
    is the sum of the two preceding ones. The @lru_cache decorator
    is used to store intermediate results, preventing the exponential
    time complexity of standard recursion and significantly improving
    performance for repeated calls.

    Args:
        n: The index in the Fibonacci sequence to calculate.

    Returns:
        The nth Fibonacci number.
    """

    # Set base cases to break recursive.
    if n <= 1:
        return n

    # Recursive call
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


# ----- Dispatcher -----
# dispatcher function is a function whose job is to decide what other function
def spell_dispatcher() -> Callable:
    """
    Creates and returns a single-dispatch spell system.

    This factory function encapsulates a generic 'spell' function that
    behaves differently depending on the type of its first argument.
    It supports integers (damage), strings (enchantments), and
    lists (multi-casts).

    Returns:
        Callable: The configured 'spell' generic function.
    """

    # The @singledispatch decorator creates the 'wrapper' object
    # and its private registry. This base function handles unknown types.
    @functools.singledispatch
    def spell(arg):
        return f"No spell available for type {type(arg).__name__}"

    # .register(int) adds an entry to the 'spell' registry mapping
    # the 'int' class to this specific implementation.
    @spell.register(int)
    def _(spell_damage: int) -> str:
        """Handles damage-based spells."""
        return f"Damage spell deals {spell_damage} damage!"

    # We use '_' as the function name because the dispatcher
    # identifies the function by its registration type, not its name,
    # so we don't care to the name.
    @spell.register(str)
    def _(enchant: str) -> str:
        """Handles enchantment-based spells."""
        return f"Enchants with '{enchant}' effect."

    @spell.register(list)
    def _(targets: List) -> str:
        """Handles multi-cast spells by iterating over a list of targets."""
        results: str = ""
        for t in targets:
            results += f"| Multi cast on {t} |"

        return results

    # Return the 'wrapper' object which now contains the full registry.
    return spell


def main() -> None:
    """Main Entrypoint"""

    # ----- Test reducing function -----

    print("\nTesting spell reducer...\n")
    spell_powers = [44, 38, 35, 38, 20, 18]
    operations = ["add", "multiply", "max", "min"]
    # Reducing the list into one object by applying
    # the operator multi times.
    for op in operations:
        result = spell_reducer(spell_powers, op)
        print(f"{op.capitalize()}: {result}")

    # We need a base function that the enchanter can "pre-fill"
    def base_enchantment(power: int, element: str, target: str) -> str:
        """Base function to test pre-fill"""
        return f"{target} is hit with {element} energy at {power} power!"

    # ----- Test partial enchanter -----
    print("\nTesting partial enchanter...\n")

    # partial_enchanter returns a dictionary of "pre-filled" functions
    enchanters: Dict[str, Callable] = partial_enchanter(base_enchantment)

    # We only need to provide the 'target' now
    # because power and element are locked!
    print(enchanters["fire_enchant"](target="🔥 Iron Sword"))
    print(enchanters["ice_enchant"](target="❄️ Wooden Shield"))
    print(enchanters["lightning_enchant"](target="⚡ Leather Boots"))

    # ----- Test memoized fibonacci -----

    print("\nTesting memoized fibonacci...\n")
    fibonacci_tests = [17, 18, 9]
    for test in fibonacci_tests:
        print(memoized_fibonacci(test))

    # ----- Test spell dispatcher -----
    print("\nTesting spell dispatcher...\n")
    # First, we call the factory function to get our "master" dispatcher
    cast = spell_dispatcher()

    # Test each type: int, str, and list
    print(cast(100))
    print(cast("Invisibility"))
    print(cast(["Orc 1", "Orc 2"]))
    print(cast(12.5))


if __name__ == "__main__":
    main()
