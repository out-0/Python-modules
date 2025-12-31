def test_achievement_tracker() -> None:
    """"""
    print("=== Achievement Tracker System ===")
    print("")
    # List player achivements
    data = {
        'alice': set(['first_kill', 'level_10',
                      'treasure_hunter', 'speed_demon']),
        'bob': set(['first_kill', 'level_10',
                    'boss_slayer', 'collector']),
        'charlie': set(['level_10', 'treasure_hunter', 'boss_slayer',
                        'speed_demon', 'perfectionist']),
        }

    players = ['alice', 'bob', 'charlie']
    for player in players:
        print(f"Player {player} achievements: {data[player]}")

    print("")
    print("=== Achievement Analytics ===")


test_achievement_tracker()
