from abc import ABC, abstractclassmethod


class Rankable(ABC):
    """"""

    @abstractclassmethod
    def calculate_rating(self) -> int:
        """"""
        pass

    @abstractclassmethod
    def update_wins(self, wins: int) -> None:
        """"""
        pass

    @abstractclassmethod
    def update_losses(self, losses: int) -> None:
        """"""
        pass

    @abstractclassmethod
    def get_rank_info(self) -> dict:
        """"""
        pass
