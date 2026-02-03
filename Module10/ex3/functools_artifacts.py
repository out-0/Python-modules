from typing import Dict, Callable
import functools
import operator

# ----- reduce function from functools module -----
def spell_reducer(spells: list[int], operation: str) -> int:
    """
    Reduces a list of spell intensities into a single value using a specified operation.

    Args:
        spells: A list of integers representing spell power levels.
        operation: The arithmetic or logical operation to apply.
                   Supported: 'add', 'multiply', 'max', 'min'.

    Returns:
        The final reduced integer value.

    Raises:
        KeyError: If the operation provided is not in the supported map.
        TypeError: If the spells list is empty (reduce requires at least one value).
    """

    # Map the supported operations to their callable fn.
    op_map: Dict[str, Callable] = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': max,
        'min': min,
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
def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    """"""



    # functools.partial lets you take an existing function
    # and pre-fill some of its arguments so you get a new
    # simpler function that only needs the rest of the arguments later.
    fire_enchant: Callable = functools.partial(base_enchantment, power=50)
    ice_enchant: Callable = functools.partial(base_enchantment, power=50)
    lightning_enchant: Callable = functools.partial(base_enchantment, power=50 element='lightning')

    return {
        'fire_enchant': fire_enchant,
        'ice_enchant': ice_enchant,
        'lightning_enchant': lightning_enchant
    }


def memoized_fibonacci(n: int) -> int
def spell_dispatcher() -> callable
