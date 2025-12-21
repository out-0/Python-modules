class Plant:
    """Blueprint of garden plants for tracking plants status"""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize each instance with provided information"""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def grow(self) -> None:
        """Grow method the increases the height of the plant by 1 cm"""
        self.height += 1

    def age_one_day(self) -> None:
        """Increase the age of the plant by 1 day"""
        self.age += 1

    def get_info(self) -> None:
        """Display the current status of the plant (name, height, age)"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


plant1 = Plant("Rose", 25, 30)
plant2 = Plant("Sunflower", 85, 45)
plant3 = Plant("Cactus", 15, 120)

plants = [plant1, plant2, plant3]

# Simulate the day 1
# And create a temporary attribute to store
# the old height to use for calculate later.
print("=== Day 1 ===")
for plant in plants:
    plant.get_info()
    plant.old_height = plant.height

day = 1
while day < 7:
    for plant in plants:
        plant.grow()
        plant.age_one_day()
    day += 1

# Simulate the day 7
print("=== Day 7 ===")
for plant in plants:
    plant.get_info()
    print(f"Growth this week: +{plant.height - plant.old_height}cm")

# Clean up temporary attributes
for plant in plants:
    del plant.old_height
