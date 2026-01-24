from ex4.TournamentCard import TournamentCard
from typing import List, Dict
from ex0.Card import Card


class TournamentPlatform:
    """"""

    def __init__(self):
        """
        Initialize the platform with base needed

        Also map a dictionary of Card_id : Card
        """

        self.registered_cards: Dict = {}

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

        self.registered_cards[card.card_id] = card
        return f"{card.card_id}: {card.name} are registered successfully"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """"""

        card1: Card = self.registered_cards.get(card1_id)
        card2: Card = self.registered_cards.get(card2_id)

        if not card1 or not card2:
                return {"error": "One or both cards not found"}

        player1_mana: int = 30
        player2_mana: int = 30
        battlefield: List = []

        card1.play({
                    'available_mana': player1_mana,
                    'battlefield': battlefield
                    })
        card2.play()

        while True:
            card1

        winner.update_

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
