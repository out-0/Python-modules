class SecurePlant:
    """Security class provide methods to protecte invalid status"""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Constructor that initialize the object with the base status
        and check for the invalid values."""
        self.name = name
        if height < 0:
            self._height = 0
        else:
            self._height = height
        if age < 0:
            self._age = 0
        else:
            self._age = age
        print(f"Plant created: {name}")

    def set_height(self, height: int) -> None:
        """Height setter that check for invalid values"""
        if height >= 0:
            self._height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age: int) -> None:
        """Age setter that check for invalid values"""
        if age >= 0:
            self._age = age
            print(f"Age updated: {age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self) -> int:
        """Height getter that return the height value"""
        return self._height

    def get_age(self) -> int:
        """Age getter that return the age value"""
        return self._age

    def get_info(self) -> None:
        """Display current information about the plant"""
        print(f"Current plant: {self.name}", end="")
        print(f" ({self._height}cm, {self._age} days)")


print("=== Garden Security System ===")
plant = SecurePlant("Rose", 20, 30)
plant.set_height(25)
plant.set_age(30)
print("")
plant.set_height(-5)
print("")
plant.get_info()
