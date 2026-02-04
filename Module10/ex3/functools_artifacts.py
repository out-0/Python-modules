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
            base_enchantment, power=50, element='fire')
    ice_enchant: Callable = functools.partial(base_enchantment, power=50,
                                              element='ice'
                                              )
    lightning_enchant: Callable = functools.partial(
                                                    base_enchantment,
                                                    power=50,
                                                    element='lightning'
                                                    )

    return {
        'fire_enchant': fire_enchant,
        'ice_enchant': ice_enchant,
        'lightning_enchant': lightning_enchant
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
        n: The index in the Fibonacci sequence to calculate (non-negative integer).

    Returns:
        The nth Fibonacci number.
    """

    # Set base cases to break recursive.
    if n <= 1:
        return n

    # Recursive call
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)



# dispatcher function is a function whose job is to decide what other function
def spell_dispatcher() -> Callable:
    """"""

    @functools.singledispatch
    def spell(arg):
        """"""
        return f"No spell available for type {type(arg).__name__}"

    @spell.register
    def _(power: int):
        """"""

        # damage spell
        return f"Damage spell deals {power * 10} damage!"

    @spell.register
    def _(enchant: str):
        """"""
        # enchantment spell
        return f"Enchants with '{enchant}' effect."

    @spell.register
    def _(targets: list):
        """"""

        # multi-cast: apply spell to each element
        results = []
        for t in targets:
            results.append(f"Multi-cast on {t}")
        return results

    return spell


# Usage
cast = spell_dispatcher()
print(cast(3))                   # int: damage
print(cast("fire"))              # str: enchant
print(cast(["orc", "troll"]))    # list: multi-cast
