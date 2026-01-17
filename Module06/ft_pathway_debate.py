from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
from alchemy.transmutation.advanced import philosophers_stone, elixir_of_life
import alchemy.transmutation

# Objective
# Understand the ancient debate between
# absolute and relative imports - two different
# paths to reach the same magical formula

print('')
print("=== Pathway Debate Mastery ===")
print('')

# Absolute imports.
print("Testing Absolute Imports (from basic.py):")

print(f"lead_to_gold(): {lead_to_gold()}")
print(f"stone_to_gem(): {stone_to_gem()}")


print('')
# Relative imports.
print("Testing Relative Imports (from advanced.py):")

print(f"philosophers_stone(): {philosophers_stone()}")
print(f"elixir_of_life(): {elixir_of_life()}")

print('')
print("Testing Package Access:")

print("alchemy.transmutation.lead_to_gold(): "
      f"{alchemy.transmutation.lead_to_gold()}")

print("alchemy.transmutation.philosophers_stone(): "
      f"{alchemy.transmutation.philosophers_stone()}")

print("Both pathways work! Absolute: clear, Relative: concise")
