from ex0.Card import Card


class ArtifactCard(Card):
    """
    Artifact card that has effect applied
    during the game and the behavior is differ,
    also often its has a durability which the
    card removed or destroyed after cost it.
    """

    # List of the current active artifacts
    active_artifacts: list = []

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
        """Playing artifact card after checking if playable
        and the current game_state

        is playable -> True, its mark as playable in the game.
        available mana -> manually safe check there is enough mana.
        durability check -> check if hit the usage limit.

        """

        try:

            if not game_state['is_playable']:
                print("This Card is not playable ❌️, often bot enough mana.")
                return {}

            if game_state['available_mana'] < self.cost:
                print("MANA: too low mana, check playable state again❕️")
                return {}

            if self.durabiliry == 0:
                print("DURABILITY is 0: Your Card is destroyed ☠️")
                return {}
        except Exception:
            print("Error detected 💣️: Accessing some stats fail")

        # If all good lets play it and activate it
        # no need for the return dict also reduce durability.
        ArtifactCard.activate_ability(self)
        self.durabiliry -= 1
        game_state['available_mana'] -= self.cost

        return {'card_played': self.name,
                'mana_used': self.cost,
                'effect': self.effect}

    def activate_ability(self) -> dict:
        """
        Activate the card effects, and return
        dictionary of them.
        """

        # Adding the card to activate list and return effect.
        ArtifactCard.active_artifacts.append(self)
        return {
            'applying': self.effect
        }
