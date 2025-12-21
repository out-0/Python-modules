class Plant:
    """Plant class represent initial information about plant"""
    def __init__(self,
                 name: str,
                 starting_height: int,
                 starting_age: int
                 ) -> None:
        """Constructor for the base elements for a plant"""
        self.name = name
        self.starting_height = starting_height
        self.starting_age = starting_age
        print(f"Created: {self.name} ", end="")
        print(f"({self.starting_height}cm, {self.starting_age} days)")


def create_plants() -> None:
    """Create 5 plants objects and initial their status"""
    plants = [
            ("Rose", 25, 30),
            ("Oak", 200, 365),
            ("Cactus", 5, 90),
            ("Sunflower", 80, 45),
            ("Fern", 15, 120)
            ]
    for name, height, age in plants:
        Plant(name, height, age)
    print("")
    print("Total plants created: 5")


print("=== Plant Factory Output ===")
create_plants()
