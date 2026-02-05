import functools
from typing import Callable, Any
import time


def spell_timer(func: Callable) -> Callable:
    """
    Decorator that measures and reports the execution time of a function.

    The decorator wraps the given callable, prints a message before execution,
    times how long the call takes, and prints the elapsed time after completion

    The original function’s metadata (__name__, __doc__) is preserved via
    functools.wraps

    Arguments:
        func (Callable): The function to be wrapped and timed.

    Returns:
        Callable: A wrapped callable function that
        returns the original function’s result.
    """

    # Decorator to preserve or save the actual meta data(__name__, __docstr__)
    # of the wrapped function so its don't change after get wrapped.
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        """Wrapper that change the behavior of the wrapped function.

        Arguments:
            - *args, **kwargs : since we don't know what that function is taken
                                so we allowed it to take whatever it want.

        Return:
            - Any : we don't know what the original function return.
        """

        print(f"Casting {func.__name__}...")

        # Count the execution time of the function.
        start = time.time()
        result: Any = func(*args, **kwargs)
        end = time.time()

        # Print the performance
        execution_time: float = end - start
        print(f"Spell completed in {execution_time:.3f} seconds")

        # Return the result returned from the original func
        return result

    # Return the wrapper callable function.
    return wrapper


def power_validator(min_power: int) -> Callable:
    """
    Make a decorator that checks a spell’s power before running it.

    This function takes a minimum power level and returns a decorator.
    When that decorator is applied to a function, it will check the
    first argument passed to the function (the power value). If the
    power is high enough (>= min_power), the original function runs.
    Otherwise, it returns a message saying the power is too low.

    Args:
        min_power (int): The minimum power required to run the spell function.

    Returns:
        Callable: A decorator that enforces the minimum power rule on
                a function
    """

    def decorator(func: Callable) -> Callable:
        """
        Wrap the given function so its first argument (power) is checked.

        This function takes the original function and returns a new function
        (wrapper) that will first check if the power argument passed to the
        function call is high enough based on the min_power value from the
        outer scope. If the power is too low, it returns a message instead
        of calling the original function.

        Args:
            func (Callable): The function being decorated.

        Returns:
            Callable: A new function that enforces the minimum power check.
        """

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            """
            Wrapper function that performs power level validation.

            This function runs when the decorated function is called. It
            compares the provided `power` to the configured `min_power`. If
            sufficient, it calls the original function with that power;
            otherwise, it returns a fallback message.

            Parameters:
                power (int): The runtime power value passed by the caller.

            Returns:
                Any: The result of the original function if validation passes,
                     or an error message if power is insufficient.
            """
            power: int = args[0]
            # Check if power is valid: execute func normally.
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """
    Create a decorator that retries a function if it fails.

    This takes a number of attempts and returns a decorator
    that will call the decorated function up to that many times
    if it keeps raising exceptions.

    Args:
        max_attempts (int): How many times to retry on failure.

    Returns:
        Callable: A decorator that will retry the wrapped function.
    """

    def decorator(func: Callable) -> Callable:
        """
        Wrap a function so it can be retried when it fails.

        This takes the function that will be called later.
        It returns a new function that tries calling the original
        function, and if it raises an exception, it retries it.

        Args:
            func (Callable): The function to be retried.

        Returns:
            Callable: A new function that handles retries.
        """

        @functools.wraps(func)
        def retry(*args, **kwargs) -> Any:
            """
            Try calling the original function up to max_attempts times.

            This is the function that gets called instead of the original.
            It tries to run the original function. If it raises an exception,
            it will print a retry message and try again until max_attempts.
            If all attempts fail, it prints a final failure message.

            Args:
                *args: Positional values passed to the wrapped function.
                **kwargs: Keyword values passed to the wrapped function.

            Returns:
                Any: The result of the original function if successful,
                    or string if all attempts fail.
            """
            i = 1
            while i <= max_attempts:
                try:
                    # I just pass the positional args to demonstrate
                    # failing later in main
                    result: Any = func(*args)
                    # If it success, return result normal
                    return result
                except Exception:
                    print(f"Spell failed, retrying... "
                          f"(attempt {i}/{max_attempts})")
                i += 1

            # If it keep failing after all attempts
            return f"Spell casting failed after {max_attempts} attempts"

        return retry

    return decorator


class MageGuild:
    """Class for mage guild"""

    def __init__(self, name: str) -> None:
        """Initial the name of the guild"""
        self.name: str = name

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """
        Check the name of the guild is valid
        valid = len > 3 | containe alpha or " "

        Arguments: name -> str

        Return: bool -> True | False
        """
        if len(name) < 3:
            return False
        for char in name:
            if not (char.isalpha() or char == " "):
                return False

        return True

    def cast_spell(self, spell_name: str, power: int) -> str:
        """
        Cast a spell after validation
        Validate the power by decorator, which will wrape it and
        execute if its valid.

        Arguments: spell_name = name to be casted
                   power = which will be validated

        Return: string that will returned from evaluation
        """

        @power_validator(10)
        def spell(power: int, spell_name: str):
            """
            Helper func which will be wraped after validation,
            if power greather or equal the validation power,
            so return the required string
            """
            return f"Successfully cast {spell_name} with power {power}"

        return (spell(power, spell_name))


def main() -> None:
    """Main Entry point"""

    # ----- Testing spell timer -----
    print("\nTesting spell timer...\n")

    # Create original function that will be wrapped.
    # And decorate it to get the wrapped func.
    @spell_timer
    def fireball() -> str:
        """Fireball spell"""
        return "Fireball cast!"

    print(fireball())

    # ----- Testing power validator -----
    print("\nTesting power validator...\n")

    @power_validator(5)
    def hit(power: int) -> str:
        """Hit something"""
        return f"Hit {power} damage successfully, Yaayyyyy 👹 "

    print(hit(6))
    print(hit(1))

    # ----- Testing retry spell -----
    print("\nTesting retry spell...\n")

    @retry_spell(3)
    def push_harder(what: str) -> str:
        """Just not raise any error its excuted and just return string"""
        return f"{what} Nope ☝️ "

    # Deomnstrate failing: by passing kwargs which not able to.
    print(push_harder(what="Anything"))

    print('')
    # Demonstrate success
    enough: str = "is that enough ?"
    print(push_harder(enough))

    # ----- Testing MageGuild -----
    print("\nTesting MageGuild...\n")
    my_guild: MageGuild = MageGuild("Morgan")
    print(my_guild.validate_mage_name("Blackdooms"))
    print(my_guild.validate_mage_name("Jo"))

    # Demonstrate two cases of casting: one success, one failed
    print(my_guild.cast_spell("Lightning", 28))
    print(my_guild.cast_spell("tornado", 5))


main()
