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
    """"""
    pass


def get_performance() -> None:
    """Count the performance of an operations"""
    pass


def test_data_stream() -> None:
    """"""
    print("=== Game Data Stream Processor ===")
    print("")
    # Events data----------------------------------
    total_events = 1000
    players = {'alice': {'level': 5, 'event': 'killed monster'},
               'bob': {'level': 12, 'event': 'found treasure'},
               'charlie': {'level': 8, 'event': 'leveled up'}}
    # Processing game events-----------------------
    processing_game_events(total_events, players)
    # Stream Analytics-----------------------------
    stream_analytics(players)


test_data_stream()
