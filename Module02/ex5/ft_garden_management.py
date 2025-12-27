class Plant:
    """Create plant with base stats"""

    def __init__(self,
                 name: int,
                 water_level: int,
                 sunlight_hours: int
                 ) -> None:
        """"""
        self.name = name
        self.water = water_level
        self.sun = sunlight_hours


class Garden:
    """Create a garden that hold plants"""

    def __init__(self) -> None:
        """"""
        self.plants = [None] * 100
        self.plants_count = 0


class GardenError(Exception):
    """A Base exception error for the garden"""
    pass


class PlantError(GardenError):
    """Specific exception for invalid plants name"""
    pass


class WaterError(GardenError):
    """Exception for water invalid vlaues"""
    pass


class SunlightError(GardenError):
    """Exception for sunlight invalid values"""
    pass


class GardenManager:
    """Create a garden manage it by its method"""

    def __init__(self, garden: object) -> None:
        """Initialize the garden with 100 plant"""
        self.garden = garden

    def add_plants(self, plant: object) -> None:
        """Check plant, if valid name == add to garden
        if not valid == raise error"""

        garden = self.garden
        plants = garden.plants
        try:
            if plant.name is None or plant.name == "":
                raise PlantError(
                        "Error adding plant: Plant name cannot be empty!"
                        )
            plants[garden.plants_count] = plant
            garden.plants_count += 1
            print(f"Added {plant.name} successfully")
        except PlantError as e:
            print(e)

    def water_plants(self) -> None:
        """Water the plants those successfully added to the garden"""

        plants = self.garden.plants
        print("Opening watering system")
        try:
            for plant in plants:
                if plant is not None:
                    print(f"Watering {plant.name} - success")
                    plant.water += 1
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self) -> None:
        """Check and raise an ValueError in invalid args cases"""

        plants = self.garden.plants
        for plant in plants:
            try:
                if plant is not None:
                    if plant.water < 1:
                        raise WaterError(
                                f"Error checking {plant.name}: "
                                f"Water level {plant.water} is too low (min 1)"
                                )
                    elif plant.water > 10:
                        raise WaterError(
                                f"Error checking {plant.name}: "
                                f"Water level {plant.water} is "
                                "too high (max 10)"
                                )
                    elif plant.sun < 2:
                        raise SunlightError(
                                f"Error checking {plant.name}: "
                                f"Sunlight hours {plant.sun} is "
                                "too low (min 2)"
                                )
                    elif plant.sun > 12:
                        raise SunlightError(
                                f"Error checking {plant.name}: "
                                f"Sunlight hours {plant.sun} "
                                "is too high (max 12)"
                                )
                    print(
                            f"{plant.name}: healthy (water: "
                            f"{plant.water}, sun: {plant.sun})"
                            )
            except (WaterError, SunlightError) as e:
                print(e)


def test_garden_management() -> None:
    """Run the demo structure"""
    print("=== Garden Management System ===")
    print("")
    # Create plants
    tomato = Plant("tomato", 4, 8)
    lettuce = Plant("lettuce", 14, 7)
    plant3 = Plant(None, 6, 7)

    print("Adding plants to garden...")
    # Create garden
    garden = Garden()
    # Create manager add add garden to manager
    manager = GardenManager(garden)
    # Add plants to garden
    manager.add_plants(tomato)
    manager.add_plants(lettuce)
    manager.add_plants(plant3)
    print("")
    # Watering the plants
    print("Watering plants...")
    manager.water_plants()
    print("")
    # check all plants health
    print("Checking plant health...")
    manager.check_plant_health()
    print("")
    # Test the recovery mincanism
    print("Testing error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("System recovered and continuing...")
    print("")
    print("Garden management system test complete!")


# Run the output
test_garden_management()
