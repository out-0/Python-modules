class Plant:
    """The base parent for the plants state"""
    def __init__(self, name, height) -> None:
        """Initial the base plants state"""
        self.name = name
        self.height = height

    def grow(self) -> None:
        """Growing a plant by 1cm"""
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_info(self) -> str:
        """Display plant stats"""
        info = f"{self.name}: {self.height}"
        return info

class FloweringPlan(Plant):
    """Specific type of plants which will produce a flowers"""
    def __init__(self, name: str, height: int, color: str, blooming: bool) -> None:
        """Initial the base state and add type additonal and blooming state"""
        super().__init__(name, height)
        self.color = color
        self.blooming = blooming

    def get_info(self) -> str:
        """Display stats of flowering plants"""
        name_and_height = f"{self.name}: {self.height}cm "
        color = f"{self.color} flowers "
        if self.blooming:
            blooming = f"(blooming)"
        else:
            blooming = f""
        return name_and_height + color + blooming

class PrizeFlower(FloweringPlan):
    """Flowering Plant with a prize state"""
    def __init__(self,
                 name: str,
                 height: int,
                 color: str,
                 blooming: bool,
                 prize_point: int
                 ) -> None:
        """Initial the base state of flowering plant
        and add additonal state of prize"""
        super().__init__(name, height, color, blooming)
        self.prize_point = prize_point

    def get_info(self) -> str:
        """Display the stats of Prize Flower"""
        name_and_height = f"{self.name}: {self.height}cm "
        color = f"{self.color} flowers "
        if self.blooming:
            blooming = f"(blooming) "
        else:
            blooming = f" "
       prize_point = f"Prize points: {self.prize_point}"
       return name_and_height + color + blooming + prize_point

class Garden:
    """Base structure of a garden"""
    def __init__(self, owner: str, garden_name: str) -> None:
        """Initial and creating garden for owner"""
        self.owner = owner
        self.garden_name = garden_name
        self.plants = []

    # add the plant object to the list of plants in a garden
    def add_plant(self, plant_object: object) -> None:
        """Add a plant to the garden"""
        self.plants.append(plant_object)
        print(f"Added {plant_object.name} to {self.garden_name} garden")

    def growing_plants(self) -> None:
        """Make all garden plants grow by 1cm"""
        plant_list = self.plants
        for plant in plant_list:
            plant.grow()
        print(f"{self.owner} is helping all plants grow...")
        for plant in plant_list:
            print(f"{plant.name} grew 1cm")

    def garden_report(self) -> None:
        """Report a current stats of a specific garden"""
        print(f"=== {self.garden_name} Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print("- ", end="")
            plant.get_info()


class GardenManager:
    """Manage the gardens"""
    def __init__(self,
                 owner_name: str,
                 garden_name: str
                 ) -> None:
        """Manage and organize the gardens"""
        gardens[owner_name] = garden_name

    class GardenStats:
        def __init__(self) -> None:
            pass

    def create_garden_network() -> None:
        pass



print("=== Garden Management System Demo ===")
print("")
# Create Alice garden
alice_garden = Garden("Alice", "Alice's")

# Create some plants
oak_tree = Plant("Oak Tree", 100)
rose = FloweringPlan("Rose", 25, "red", True)
sun_flower = PrizeFlower("Sunflower", 50, "yellow", True, 10)

print("")

# Add plants to Alice's garden
alice_garden.add_plant(oak_tree)
alice_garden.add_plant(rose)
alice_garden.add_plant(sun_flower)

print("")

# Growing the plants in garden
alice_garden.growing_plants()
# Report the garden stats
alice_garden.garden_report()
