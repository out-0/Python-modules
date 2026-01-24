from ex4.TournamentCard import TournamentCard
from typing import List, Dict
from ex0.Card import Card


class TournamentPlatform:
    """"""

    def __init__(self):
        """
        Initialize the platform with base needed
        """

        self.registered_cards: List = []

    def register_card(self, card: TournamentCard) -> str:
        """
        Before cards can make a match they need to be
        registered
        """

        if not card:
            print("Error: Invalid card provided ❌️")
            return
        if not isinstance(card, TournamentCard):
            print("Warring: Your Card not able to apply for Tournament")
            return

        self.registered_cards.append(card)
        return "{card.name} are registered successfully"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """"""
        card1: Card = [
                       card for card in self.registered_cards
                       if card.card_id == card1_id
                      ]
        card2: Card = [
                       card for card in self.registered_cards
                       if card.card_id == card2_id
                      ]

        cards: List[Card] = [card1, card2]

        battlefield: List = []
        player1_mana: int = 30
        player2_mana: int = 30
        is_playable: bool = False

        game_state: Dict = {
                            'is_playable': is_playable,
                            'battlefield': battlefield,
                            'available_mana': None
                            }

        # List of kinda players map their mana and cards to play

        for player in players:
            current_mana = player["mana"]
            current_card = player["card"]

            # Update the state first
            game_state['available_mana'] = current_mana

            # Now pass the actual dictionary, not the result of an update() call
            result = current_card.play(game_state)

        for card in cards:
            card.play()

    def get_leaderboard(self) -> list:
        """"""
        pass

    def generate_tournament_report(self) -> dict:
        """"""
        pass
