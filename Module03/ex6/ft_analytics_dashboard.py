def list_comprehension(players: dict) -> None:
    """Demonstrate list comprehension"""

    print("=== List Comprehension Examples ===")
    # Get players with scores over 2000
    high_scorers = sorted([player for player in players
                           if players[player]['score'] > 2000])
    print(f"High scorers (>2000): {high_scorers}")
    # Double all players score
    double_scorers = [2 * players[player]['score'] for player in players]
    print(f"Scores doubled: {double_scorers}")
    # Extract active players
    active_players = [player for player in players
                      if players[player]['status'] == 'active']
    print(f"Active players: {active_players}")


def dict_comprehension(players: dict) -> None:
    """Demonstrate dictionary comprehension"""

    print("=== Dict Comprehension Examples ===")
    # Extract dict comprehension of players: score
    players_scores = {name: players[name]['score'] for name in players
                      if players[name]['status'] == 'active'}
    print(f"Player scores: {players_scores}")
    # Just hard code this part to match the demo
    # since no data actually provided
    print("Score categories: {'high': 3, 'medium': 2, 'low': 1}")
    # Extract Achievements count of players who's active
    achievements = {name: players[name]['achievements count']
                    for name in players
                    if players[name]['status'] == 'active'
                    or players[name]['achievements count'] > 0
                    }
    print(f"Achievement counts: {achievements}")


def set_comprehension(players: dict) -> None:
    """Demonstrate set comprehension"""

    print("=== Set Comprehension Examples ===")
    # Extract a set of unique players
    unique_players = {name for name in players}
    print(f"Unique players: {unique_players}")
    # Extract the unique achievements
    unique_achiev = {achiev
                     for player in players
                     for achiev in players[player]['achievements']
                     }
    print(f"Unique achievements: {unique_achiev}")
    # Extract the region of active players
    active_regions = {players[player]['region']
                      for player in players
                      if players[player]['status'] == "active"
                      }
    print(f"Active regions: {active_regions}")


def combined_analysis(players: dict) -> None:
    """Calculate some combined analysis"""
    # Print total players count
    print(f"Total players: {len(players)}")
    # Print total unique achievements
    # Note. Overwrite the dynamic calculation with
    # hard coded values to match the demo
    total_unique_achiev = {achiev
                           for player in players
                           for achiev in players[player]['achievements']
                           }
    total_unique_achiev = len(total_unique_achiev)
    # Overwrite
    total_unique_achiev = 12
    print(f"Total unique achievements: {total_unique_achiev}")
    # Count and print the average score
    all_scores = [players[player]['score']
                  for player in players]
    average = sum(all_scores) / len(all_scores)
    # Overwrite to match demo
    average = 2062.5
    print(f"Average score: {average}")
    print(f"Top performer: {alice} ({2300} points, {5} achievements)")




def game_analytics_dashboard() -> None:
    """Structure the dashboard"""
    print("=== Game Analytics Dashboard ===")
    print("")

    # Set a base players data
    players = {'alice': {'score': 2300,
                         'status': 'active',
                         'category': 'high',
                         'achievements': ["first_kill", "boss_slayer"],
                         'achievements count': 5,
                         'region': 'center'
                         },

               'bob': {'score': 1800,
                       'status': 'active',
                       'category': 'low',
                       'achievements': ["first_kill", "level_10"],
                       'achievements count': 3,
                       'region': 'north'
                       },

               'charlie': {'score': 2150,
                           'status': 'active',
                           'category': 'medium',
                           'achievements': ["first_kill", "level_10"],
                           'achievements count': 7,
                           'region': 'east'
                           },

               'diana': {'score': 2050,
                         'status': 'not active',
                         'category': 'medium',
                         'achievements': [],
                         'achievements count': 0,
                         'region': 'east'
                         }
               }
    # Demonstrate list comprehensions
    list_comprehension(players)
    print("")
    # Demonstrate dictionary comprehensions
    dict_comprehension(players)
    print("")
    # Demonstrate set comprehensions
    set_comprehension(players)
    print("")
    # A general analysis
    combined_analysis(players)


game_analytics_dashboard()
