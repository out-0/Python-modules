class GardenError(Exception):
    """Base Garden errors that inherit from the Exception
    so its be raise-able """
    pass


class PlantError(GardenError):
    """Plant error type that inherit
    from base garden error class"""
    pass


class WaterError(GardenError):
    """Water error type that inherit
    from base garden error class"""
    pass


def check_plant(plant_name: str) -> None:
    """Check and raise the plant error"""
    raise PlantError(f"The {plant_name} plant is wilting")


def check_water(tank_state: str) -> None:
    """Check and raise the water error"""
    if tank_state == "empty":
        raise WaterError("Not enough water in the tank!")


print("=== Custom Garden Errors Demo ===")
print("")
try:
    print("Testing PlantError...")
    check_plant("tomato")
except PlantError as e:
    print(f"Caught PlantError: {e}")
print("")
try:
    print("Testing WaterError...")
    check_water("empty")
except WaterError as e:
    print(f"Caught WaterError: {e}")
print("")
print("Testing catching all garden errors...")
checks = [
        (check_plant, "tomato"),
        (check_water, "empty")
        ]
for function, arg in checks:
    try:
        function(arg)
    except GardenError as e:
        print(f"Caught a garden error: {e}")

print("")
print("All custom error types work correctly!")
