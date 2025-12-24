class Plant:
    """The base parent for the plants state"""
    def __init__(self, name: str, height: int) -> None:
        """Initial the base plants state"""
        self.name = name
        self.height = height
        self.type = "regular"

    def grow(self, grow_size: int) -> int:
        """Growing a plant by 1cm by default if the
        user doesn't explicit the size of growth"""
        self.height += grow_size
        print(f"{self.name} grew {grow_size}cm")
        return (grow_size)

    def get_info(self) -> str:
        """Display plant stats"""
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """Specific type of plants which will produce a flowers"""
    def __init__(self,
                 name: str,
                 height: int,
                 color: str,
                 blooming: bool
                 ) -> None:
        """Initial the base state and add type additional and blooming state"""
        super().__init__(name, height)
        self.color = color
        self.blooming = blooming
        self.type = "flowering"

    def get_info(self) -> str:
        """Display stats of flowering plants"""
        base_info = super().get_info()
        color = f", {self.color} flowers "
        if self.blooming:
            blooming = "(blooming)"
        else:
            blooming = ""
        return base_info + color + blooming


class PrizeFlower(FloweringPlant):
    """Flowering Plant with a prize state"""
    def __init__(self,
                 name: str,
                 height: int,
                 color: str,
                 blooming: bool,
                 prize_point: int
                 ) -> None:
        """Initial the base state of flowering plant
        and add Additional state of prize"""
        super().__init__(name, height, color, blooming)
        self.prize_point = prize_point
        self.type = "prize"

    def get_info(self) -> str:
        """Display the stats of Prize Flower"""
        base_info = super().get_info()
        prize_point = f", Prize points: {self.prize_point}"
        return base_info + prize_point


class Garden:
    """Base structure of a garden"""
    def __init__(self, owner: str, garden_name: str) -> None:
        """Initial and creating garden for owner"""
        self.owner = owner
        self.garden_name = garden_name
        list_size = 100
        self.plants = [None] * list_size
        self.plants_count = 0
        self.total_growth = 0
        self.regular_plants = 0
        self.flowering_plants = 0
        self.prize_plants = 0

    # add the plant object to the list of plants in a garden
    def add_plant(self, plant_object: object, silent: bool = False) -> None:
        """Add a plant to the garden plants list by indexing"""
        self.plants[self.plants_count] = plant_object
        self.plants_count += 1
        # Calculating the plant types
        if plant_object.type == "regular":
            self.regular_plants += 1
        elif plant_object.type == "flowering":
            self.flowering_plants += 1
        elif plant_object.type == "prize":
            self.prize_plants += 1
        if not silent:
            print(f"Added {plant_object.name} to {self.garden_name} garden")

    def growing_plants(self, growth_size: int = 1) -> None:
        """Make all garden plants grow"""
        print(f"{self.owner} is helping all plants grow...")
        plant_list = self.plants
        for plant in plant_list:
            if plant is not None:
                self.total_growth += plant.grow(growth_size)

    def garden_report(self) -> None:
        """Report a current stats of a specific garden"""
        print(f"=== {self.garden_name} Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            if plant is not None:
                print(f"- {plant.get_info()}")
        print("")
        # Printing the formatted result
        print(f"Plants added: {self.plants_count}, ", end="")
        print(f"Total growth: {self.total_growth}cm")
        regular = f"Plant types: {self.regular_plants} regular, "
        flowering = f"{self.flowering_plants} flowering, "
        prize = f"{self.prize_plants} prize flowers"
        print(regular + flowering + prize)


class GardenManager:
    all_managers = [None] * 100
    managers_count = 0

    """Manage the gardens"""
    def __init__(self) -> None:
        """Create and track a list of gardens"""
        self.gardens_list = [None] * 100
        self.gardens_count = 0
        # That for managers network later.
        GardenManager.all_managers[GardenManager.managers_count] = self
        GardenManager.managers_count += 1

    def add_garden(self, garden: object) -> None:
        """Add a specific garden to the manager list of gardens"""
        self.gardens_list[self.gardens_count] = garden
        self.gardens_count += 1

    class GardenStats:
        """Calculate some base statistics about a garden"""
        def __init__(self, manager: object) -> None:
            """Initializer for nested class"""
            self.gardens_list = manager.gardens_list
            self.gardens_count = manager.gardens_count

        def is_valid_height(height: int) -> int:
            """Static method to check the validation of height"""
            if height < 0:
                return 0
            else:
                return 1
        # Converting the class method to regular one.
        is_valid_height = staticmethod(is_valid_height)

        def is_valid_gardens_heights(cls, gardens_list: list) -> bool:
            """Iterate on all plants in all gardens and check their height"""
            valid_heights = 1
            all_gardens = gardens_list
            for garden in all_gardens:
                if garden is not None:
                    for plant in garden.plants:
                        if plant is not None:
                            valid_heights = cls.is_valid_height(plant.height)
                            if not valid_heights:
                                return False
            return True
        # Convert it to a class method.
        is_valid_gardens_heights = classmethod(is_valid_gardens_heights)

        def parse_and_display_stats(self) -> None:
            """Parse the stats and display the result"""
            for garden in self.gardens_list:
                if garden is not None:
                    garden.score = garden.plants_count * 10
                    for plant in garden.plants:
                        if plant is not None:
                            garden.score += plant.height
                            if plant.type == "prize":
                                garden.score += plant.prize_point
            # check the valiadation of all gardens heights
            height_stats = self.is_valid_gardens_heights(self.gardens_list)
            print(f"Height validation test: {height_stats}")
            print("Garden scores - ", end="")
            i = 0
            while self.gardens_list[i] is not None:
                print(f"{self.gardens_list[i].owner}: ", end="")
                print(f"{self.gardens_list[i].score}", end="")
                if self.gardens_list[i + 1] is not None:
                    print(", ", end="")
                i += 1
            print("")
            print(f"Total gardens managed: {self.gardens_count}")

    def create_garden_network(cls) -> None:
        """Create a garden network and return the gardens"""
        print("Garden network initialized ", end="")
        print(f"with {cls.managers_count} managers")
        return cls.all_managers
    create_garden_network = classmethod(create_garden_network)


print("=== Garden Management System Demo ===")
print("")

# -- Create a Garden Manager --
manager = GardenManager()

# -- Create Alice's garden and add plants
alice_garden = Garden("Alice", "Alice's")
# -- Create some plants for Alice's garden
oak_tree = Plant("Oak Tree", 100)
rose = FloweringPlant("Rose", 25, "red", True)
sun_flower = PrizeFlower("Sunflower", 50, "yellow", True, 10)
# -- Add plants to Alice's garden
alice_garden.add_plant(oak_tree)
alice_garden.add_plant(rose)
alice_garden.add_plant(sun_flower)
print("")
# -- Growing the plants in garden
alice_garden.growing_plants()
print("")
# -- Report the garden stats
alice_garden.garden_report()
print("")

# -- Create Bob's garden and add plants
bob_garden = Garden("Bob", "Bob's")
# -- Create some plants for Bob's garden
cactus = Plant("Cactus", 30)
daffodil = Plant("Daffodil", 42)
# -- Add plants to Bob's garden silently
bob_garden.add_plant(cactus, silent=True)
bob_garden.add_plant(daffodil, silent=True)

# -- Add the gardens to the manager
manager.add_garden(alice_garden)
manager.add_garden(bob_garden)

# -- Pass the garden to calculate its stats
stats = manager.GardenStats(manager)
stats.parse_and_display_stats()
