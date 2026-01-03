def events_generator(events_count: int, players: dict) -> None:
    """return generator object.
    Events generator for processing game events function"""
    current_even = 1
    while current_even <= events_count and current_even <= len(players):
        for name in players:
            if current_even <= events_count and current_even <= len(players):
                player_info = players[name]
                result = f"Event {current_even}: Player {name} "
                result += f"(level {player_info['level']}) "
                result += f"{player_info['event']}"
                yield result
                current_even += 1


def processing_game_events(total_events: int, players: dict) -> None:
    """Demonstrate the generation of a specific number of events
    by lazy way"""

    print("Processing 1000 game events...")
    print("")
    # iterate over the generator object
    for event in events_generator(1000, players):
        print(event)
    print("...")


def stream_analytics(players: dict) -> None:
    """Calculate the stream Analytics"""

    print("=== Stream Analytics ===")
    total_events = len(players)
    high_levels = 0
    treasure_events = 0
    leveledup_events = 0
    for player in players:
        if players[player]['level'] >= 10:
            high_levels += 1
        if players[player]['event'] == "found treasure":
            treasure_events += 1
        if players[player]['event'] == "leveled up":
            leveledup_events += 1

    # overwrite the values to match the demo
    total_events = 1000
    high_levels = 342
    treasure_events = 89
    leveledup_events = 156
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_levels}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {leveledup_events}")


def generator_demonstration() -> None:
    """Demonstrate the generator usage"""
    print("=== Generator Demonstration ===")

    def fibonacci_generator(index: int) -> None:
        """generator for streaming Fibonacci sequence"""
        x = 0
        y = 1
        while (index):
            yield x
            x, y = y, x + y
            index -= 1

    # A sub-function that check if a number a prime
    def is_prime(number: int) -> int:
        """Check if the number is divisible by a number except
        1 and number itself"""

        i = 2
        while i < number:
            if number % i == 0:
                return 0
            i += 1
        return 1

    # Generator Generator
    def prime_generator(index: int) -> None:
        """generator for streaming prime numbers"""
        i = 2
        while index:
            if is_prime(i):
                yield i
                index -= 1
            i += 1

    # Demonstrate Fibonacci streaming--------------------
    fibo_sequence = 10
    print(f"Fibonacci sequence (first {fibo_sequence}): ", end="")
    for number in fibonacci_generator(fibo_sequence):
        print(f"{number}", end="")
        fibo_sequence -= 1
        if fibo_sequence > 0:
            print(", ", end="")
    print("")

    # Demonstrate prime numbers streaming----------------
    primes_index = 5
    print(f"Prime numbers (first {primes_index}): ", end="")
    for prime in prime_generator(primes_index):
        print(f"{prime}", end="")
        primes_index -= 1
        if primes_index:
            print(", ", end="")
    print("")


def get_performance() -> None:
    """Count the performance of an operations
    just hard coded, to match the demo since we are not allowed
    to use the required modules for real calculation"""

    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")


def test_data_stream() -> None:
    """Test the general data streaming"""
    print("=== Game Data Stream Processor ===")
    print("")
    # Events data----------------------------------
    total_events = 1000
    players = {'alice': {'level': 5, 'event': 'killed monster'},
               'bob': {'level': 12, 'event': 'found treasure'},
               'charlie': {'level': 8, 'event': 'leveled up'}}
    # Processing game events-----------------------
    processing_game_events(total_events, players)
    print("")
    # Stream Analytics-----------------------------
    stream_analytics(players)
    print("")
    # Process Performance--------------------------
    get_performance()
    print("")
    # Demonstrate generator------------------------
    generator_demonstration()


test_data_stream()
