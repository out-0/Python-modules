from abc import ABC, abstractmethod


class Combatable(ABC):
    """
    Combatable category which provide
    an abstract interface
    """

    @abstractmethod
    def attack(self, target):
        """attack interface for other
        specialized Combatable types"""
        pass

    @abstractmethod
    def defend(self, incoming_damage: int):
        """defend interface for other
        specialized Combatable types"""
        pass

    @abstractmethod
    def get_combat_stats(self):
        """Return a snapshot of the stats
        of comabat interface"""
        pass
