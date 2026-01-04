def list_comprehension(players: dict) -> None:
    """Demonstrate list comprehension"""

    print("=== List Comprehension Examples ===")
    # Get players with scores over 2000
    high_scorers = [player for player in players if players[player] > 2000]
    print(f"High scorers (>2000): {high_scorers}")
    # Double all players score
    double_scorers = [for player in players[player] return players[player][0]]
    print(double_scorers)
    #Scores doubled: [4600, 3600, 4300, 4100]


def dict_comprehension(players: dict) -> None:
    """Demonstrate dictionary comprehension"""


def set_comprehension(players: dict) -> None:
    """Demonstrate set comprehension"""


def game_analytics_dashboard() -> None:
    """Structure the dashboard"""
    print("=== Game Analytics Dashboard ===")
    print("")

    # Set a base players data
    players = {'alice': 2300,
               'bob': 1800,
               'charlie': 2150,
               'diana': 2050}
    list_comprehension(players)


game_analytics_dashboard()
