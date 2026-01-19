from ex0.Card import Card


class ArtifactCard(Card):
    """
    Artifact card that has effect applied
    during the game and the behavior is differ,
    also often its has a durability which the
    card removed or destroyed after cost it.
    """

    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 durability: int,
                 effect: str
                 ) -> None:
        """Initialize the base stats for an artifact card:

        - Name
        - Cost
        - Rarity
        - Durability (the times can card be used)
        - Effect


        """

        super().__init__(name, cost, rarity)
        self.durabiliry: int = durability  # how much time can card used.
        self.effect: str = effect

    def play(self, game_state: dict) -> dict:
        """"""
        pass

    def activate_ability(self) -> dict:
        """"""
        pass
