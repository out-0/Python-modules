import alchemy

# Objective:
# Discover the power of __init__.py - the sacred Scroll
# that transforms ordinary folders into magical Python packages.

print('')
print("=== Sacred Scroll Mastery ===")
print('')


print("Testing direct module access:")

fire_result: str = alchemy.elements.create_fire()
print(f"alchemy.elements.create_fire() : {fire_result}")

water_result = str = alchemy.elements.create_water()
print(f"alchemy.elements.create_water() : {water_result}")

earth_result = str = alchemy.elements.create_earth()
print(f"alchemy.elements.create_earth() : {earth_result}")

air_result = str = alchemy.elements.create_air()
print(f"alchemy.elements.create_air() : {air_result}")


print('')
# Package-level access:
# Demonstrate direct access to the element got
# initialized with the __init__ file.
print("Testing package-level access (controlled by __init__.py):")

fire_access: str = alchemy.create_fire()
print(f"alchemy.create_fire(): {fire_access}")

water_access: str = alchemy.create_water()
print(f"alchemy.create_water(): {water_access}")


try:
    # This will file since the earth still hidden,
    # which mean doesn't imported in __init__
    earth_access = alchemy.create_earth()

except AttributeError:
    earth_access: str = "AttributeError - not exposed"

# Print the result dynamically.
print(f"alchemy.create_earth(): {earth_access}")


try:
    # Same here.
    air_access = alchemy.create_air()

except AttributeError:
    air_access: str = "AttributeError - not exposed"

print(f"alchemy.create_air(): {air_access}")


print('')
# Print meta data assigned to module object.
print("Package metadata:")

print(f"Version: {alchemy.__version__}")
print(f"Author: {alchemy.__author__}")
