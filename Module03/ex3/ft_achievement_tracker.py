def test_achievement_tracker() -> None:
    """Track the achievements between tree players"""
    print("=== Achievement Tracker System ===")
    print("")
    # List player achievement's
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

    alice = data['alice']
    bob = data['bob']
    charlie = data['charlie']

    # Extract distinct achievements
    distinct_achievs = alice.union(bob, charlie)
    print(f"All unique achievements: {distinct_achievs}")
    print(f"Total unique achievements: {len(distinct_achievs)}")
    print("")
    common_achievs = alice.intersection(bob, charlie)
    print(f"Common to all players: {common_achievs}")
    # Rare (unique) achievement for each player
    player1 = alice.difference(bob, charlie)
    player2 = bob.difference(alice, charlie)
    player3 = charlie.difference(alice, bob)
    # Extract a rare achievement's set
    rare_achievements = player1.union(player2, player3)
    print(f"Rare achievements (1 player): {rare_achievements}")
    print("")
    # The intersection (common) between alice and bob
    alice_common_bob = alice.intersection(bob)
    print(f"Alice vs Bob common: {alice_common_bob}")
    alice_unique = alice.difference(bob)
    print(f"Alice unique: {alice_unique}")
    bob_unique = bob.difference(alice)
    print(f"Bob unique: {bob_unique}")


test_achievement_tracker()
