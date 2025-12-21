class Plant:
    """Base Plant class"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Constructor for the initial data"""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """Flower that has a status and ability to bloom"""
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initializer for the base flower state
        by the super function that follow the MRO"""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Display the blooming message"""
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> None:
        """Display flower state"""
        print(f"{self.name} (Flower): ", end="")
        print(f"{self.height}cm, {self.age} days, {self.color} color")


class Tree(Plant):
    """Tree that has trunk diameter and can produce shade"""
    def __init__(self, name: str,
                 height: int,
                 age: int,
                 trunk_diameter: int
                 ) -> None:
        """Constructor for tree base state"""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self, size: int) -> None:
        """Produce a tree shade with size square meters"""
        print(f"{self.name} provides {size} square meters of shade")

    def get_info(self) -> None:
        """Display tree state"""
        print(f"{self.name} (Tree): ", end="")
        print(f"{self.height}cm, {self.age} days, ", end="")
        print(f"{self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    """Vegetable with harvest season and nutritional value"""
    def __init__(self,
                 name: str,
                 height: int,
                 age: int,
                 harvest_season: str,
                 nutritional_value: str
                 ) -> None:
        """Initializer method with vegetable base state"""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> None:
        """Display the Vegetable state"""
        print(f"{self.name} (Vegetable): ", end="")
        print(f"{self.height}cm, {self.age} days, ", end="")
        print(f"{self.harvest_season} harvest")
        print(f"{self.name} is rich in {self.nutritional_value}")


# Flowers instances
flower_rose = Flower("Rose", 25, 30, "red")
flower_Alyssum = Flower("Alyssum", 30, 45, "white")

# Tree's instances
tree_oak = Tree("Oak", 500, 1825, 50)
tree_mok = Tree("mok", 340, 1023, 42)

# Vegetables instances
vegetable_tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
vegetable_carrot = Vegetable("Carrot", 40, 75, "Autumn", "vitamin A")

print("=== Garden Plant Types ===")
print("")
flower_rose.get_info()
flower_rose.bloom()
print("")
tree_oak.get_info()
tree_oak.produce_shade(78)
print("")
vegetable_tomato.get_info()
