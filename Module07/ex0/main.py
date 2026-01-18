from ex0.CreatureCard import CreatureCard

print('')
print("=== DataDeck Card Foundation ===")
print('')
print("Testing Abstract Base Class Design:")
print('')

# Create the dragon which a Creature card[Name, cost, rarity, attack, health]
fire_dragon: CreatureCard = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

print("CreatureCard Info:")
print(fire_dragon.get_card_info())

print('')
available_mana: int = 6
print(f"Playing Fire Dragon with {available_mana} mana available:")

# Check if that Card can be played which the current available_mana.
print(f"Playable: {fire_dragon.is_playable(available_mana)}")

# Print the playing result
playing_dragon_result: Dict = fire_dragon.play({})
print(f"Play result: {playing_dragon_result}")

