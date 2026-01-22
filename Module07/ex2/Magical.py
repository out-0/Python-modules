from abc import ABC, abstractmethod


class Magical(ABC):
    """Magical interface for specialized who has
    magical power."""

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list):
        """The power of casting spells on a multi targets"""
        pass

    @abstractmethod
    def channel_mana(self, amount: int):
        """Channel mana(recover) provide interface
        to recover some mana from your pool"""
        pass

    @abstractmethod
    def get_magic_stats(self):
        """A snapshot of the stats of magical interface"""
        pass
