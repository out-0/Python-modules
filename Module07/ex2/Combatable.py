from abc import ABC, abstractmethod


class Combatable(ABC):

    def __init__(self):
        """"""
        pass
    pass

    @abstractmethod
    def attack(self, target):
        pass

    @abstractmethod
    def defend(self, incoming_damage: int):
        pass

    @abstractmethod
    def get_combat_stats(self):
        pass

