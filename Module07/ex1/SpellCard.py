from ex0.Card import Card


class SpellCard(Card):
    """
    Spelling Cards a player may activate and Set
    during their turn 🪄
    Spell Cards not have attack or health stats,
    they are often just have effects.

    """

    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 effect_type: str
                 ) -> None:
        """Initialize the spell card base stats
        from the parent(Card) and append some special
        stats.

        All stats:

        - name
        - cost
        - rarity
        - effect (the effect of the card)

        """
        super().__init__(name, cost, rarity)
        self.effect_type: str = effect_type

    # Override play abstract method.
    def play(self, game_state: dict) -> dict:
        """Return playing stats

        Checks:

        - Check if playable.
        - Check actual state game available mana.

        return dictionary hold:

        - Spell name
        - Mana Cost of that Spell
        - Effect that applied by that Spell

        """

        if not game_state['is_playable']:
            print("This Card is not playable ❌️, offten not enough mana.")
            return {}

        if game_state['available_mana'] < self.cost:
            print("MANA: too low mana, check playable state again❕️")
            return {}

        # If all good lets play it
        game_state['available_mana'] -= self.cost

        return {'card_played': self.name,
                'mana_used': self.cost,
                'effect': self.effect_type}

    def resolve_effect(self, targets: list) -> dict:
        """"""
        pass
