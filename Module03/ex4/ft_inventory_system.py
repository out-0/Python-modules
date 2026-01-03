def parse_analytics(players: dict) -> None:
    """Count the Analytics of players"""
    print("=== Inventory Analytics ===")
    # dictionary to store the players inventory values
    player_values_list = {}
    rarest_items = [None] * 100
    index = 0
    for player in players:
        result = 0
        most_items = 0
        for key, values in players[player].items():
            prize = values.get('prize', 0)
            quantity = values.get('quantity', 0)
            result += prize * quantity
            most_items += quantity
            check_rarest = values.get('rarity', 0)
            if check_rarest in ("rare", "epic", "legnedary"):
                rarest_items[index] = key
                index += 1
        player_values_list.update({player: {'value': result,
                                            'most_items': most_items}})

    # Compare and print the winner
    alice_values = player_values_list['alice'].get('value')
    bob_values = player_values_list['bob'].get('value')
    if alice_values >= bob_values:
        print(f"Most valuable player: Alice ({alice_values} gold)")
    else:
        print(f"Most valuable player: Bob ({bob_values} gold)")
    alice_items = player_values_list['alice'].get('most_items')
    bob_items = player_values_list['bob'].get('most_items')
    if alice_items > bob_items:
        print(f"Most items: Alice ({alice_items} items)")
    else:
        print(f"Most items: Bob ({bob_items} items)")
    # --Print Rarest items--
    print("Rarest items: ", end="")
    jndex = 0
    while jndex < index:
        print(rarest_items[jndex], end="")
        jndex += 1
        if jndex != index:
            print(", ", end="")
    print("")


def test_inventory_system() -> None:
    """Organize a RBG system inventory and structure the values"""
    print("=== Player Inventory System ===")
    print("")
    # Players inventory
    players = {
            'alice': {
                'sword': {'category': "weapon",
                          'rarity': "rare",
                          'prize': 500,
                          'quantity': 1},
                'potion': {'category': "consumable",
                           'rarity': "common",
                           'prize': 50,
                           'quantity': 5},
                'shield': {'category': "armor",
                           'rarity': "uncommon",
                           'prize': 200,
                           'quantity': 1}
                },
            'bob': {
                'magic_ring': {'category': 'custom',
                               'rarity': 'rare',
                               'prize': 501},
                }
            }
    print("=== Alice's Inventory ===")
    # Extract the key list
    keys = players['alice'].keys()
    # Print alice inventory:
    for key in keys:
        equipment = players['alice'][key].get('category')
        equipment_rarity = players['alice'][key].get('rarity')
        equipment_quantity = players['alice'][key].get('quantity')
        equipment_prize = players['alice'][key].get('prize')
        print(f"{key} ({equipment}, {equipment_rarity}): "
              f"{equipment_quantity}x @ {equipment_prize} "
              f"gold each = {equipment_prize * equipment_quantity} gold")
    print("")
    # Extract the value of the inventory
    total_inventory_value = 0
    item_count = 0
    for item_info in players['alice'].values():
        prize = item_info['prize']
        quantity = item_info['quantity']
        total_inventory_value += prize * quantity
        item_count += quantity
    print(f"Inventory value: {total_inventory_value} gold")
    print(f"Item count: {item_count} items")

    # Extract categories and their count
    categories_count = dict()
    for value in players['alice'].values():
        current_category = value['category']
        current_quantity = value['quantity']
        # Check if the key already exist sum the quantity and update,
        # otherwise use update to add the new key
        exist = categories_count.get(current_category)
        if not exist:
            categories_count.update({current_category: current_quantity})
        else:
            exist_quantity = categories_count.get(current_category)
            new_quantity = exist_quantity + current_quantity
            categories_count.update({current_category: new_quantity})

    print("Categories: ", end="")
    # Loop on the keys in the new dictionary and format the output
    keys_list = categories_count.keys()
    index = 0
    for key in keys_list:
        print(f"{key}({categories_count[key]})", end="")
        index += 1
        if index != len(keys_list):
            print(", ", end="")
        else:
            print()

    print("")
    print("=== Transaction: Alice gives Bob 2 potions ===")
    # Check if can alice give bob some potions and behave based on the result
    # also check if bob doesn't have potion set result 0 so initialized later.
    alice_potion_quantity = players['alice']['potion'].get('quantity')
    gived_quantity = 2

    if alice_potion_quantity >= gived_quantity:
        can_give_to_bob = True
    else:
        can_give_to_bob = False
    if can_give_to_bob:
        new_alice_quantity = alice_potion_quantity - gived_quantity
        players['alice']['potion'].update({'quantity': new_alice_quantity})
        players['bob'].update({'potion': {'category': "consumable",
                                          'rarity': "common",
                                          'prize': 50,
                                          'quantity': gived_quantity}})
        print("Transaction successful!")
        print("")
        print("=== Updated Inventories ===")
        print(f"Alice potions: {new_alice_quantity}")
        new_bob_quantity = players['bob']['potion'].get('quantity', 0)
        print(f"Bob potions: {new_bob_quantity}")
    else:
        print("Well, alice also broke, go find some")
    print("")
    parse_analytics(players)


test_inventory_system()
