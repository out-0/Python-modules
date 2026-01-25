from ex4.TournamentCard import TournamentCard
from typing import List, Dict
from ex0.Card import Card


class TournamentPlatform:
    """
    Platform that manage and organize
    registration of tournament cards
    ant there matches
    """

    def __init__(self):
        """
        Initialize the platform with base needed

        Also map a dictionary of Card_id : Card
        """

        self.registered_cards: Dict = {}
        self.matches_played: int = 0

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
        """
        Create a match between two cards and report the winner with some
        useful information:

        - Winner
        - Loser
        - Winner rating
        - Loser rating
        """

        # Get the actual cards based on they Ids
        card1: Card = self.registered_cards.get(card1_id)
        card2: Card = self.registered_cards.get(card2_id)

        if not card1 or not card2:
            return {"error": "One or both cards not found"}

        # Initialize some starting data
        player1_mana: int = 30
        player2_mana: int = 30
        battlefield: List = []
        winner: str = ""

        # Play the provided Cards
        card1.play({
                    'available_mana': player1_mana,
                    'battlefield': battlefield
                    })
        card2.play({
                    'available_mana': player2_mana,
                    'battlefield': battlefield
                    })

        while True:
            # Attack by first card and check if it win.
            card1.attack(card2)
            if card2.health_value <= 0:
                winner: str = card1
                loser: str = card2
                card1.update_wins(1)
                card2.update_losses(1)
                break

            # Attack by second card and check if it win.
            card2.attack(card1)
            if card1.health_value <= 0:
                winner: str = card2
                loser: str = card1
                card2.update_wins(1)
                card1.update_losses(1)
                break

        # Track matches played
        self.matches_played += 1
        card1.total_matches += 1
        card2.total_matches += 1

        # Restore the starting health since so can
        # play matches later fresh
        card1.health_value: int = card1.health_for_rating
        card2.health_value: int = card2.health_for_rating

        return {
                'winner': winner.card_id,
                'loser': loser.card_id,
                'winner_rating': winner.calculate_rating(),
                'loser_rating': loser.calculate_rating()
                }

    def get_leaderboard(self) -> list:
        """
        Format the cards information
        and return them as a string list
        """

        leaderboard_list: List[str] = []
        all_cards: List[Card] = list(self.registered_cards.values())

        def return_rating(card: TournamentCard):
            """Just helper function return rating of card for sort"""
            return card.calculate_rating()

        # Sort cards to be sorted for leaderboard
        all_cards.sort(key=return_rating, reverse=True)

        # Extracting card to access its info
        i: int = 1
        for card in all_cards:
            formatted: str = (f"{i}. {card.name} - Rating: "
                              f"{card.calculate_rating()} "
                              f"({card.wins}-{card.losses})")
            leaderboard_list.append(formatted)
            i += 1

        return leaderboard_list

    def generate_tournament_report(self) -> dict:
        """
        Get a Big overview about the tournament representing
        a useful information
        """
        all_ratings: int = 0

        # Extract list of cards from that mapped dictionary
        all_cards: List = list(self.registered_cards.values())

        # Sum all the ratings
        all_ratings = sum([card.calculate_rating() for card in all_cards])

        # // get just the int without decimal.
        avg_rating: int = all_ratings // len(all_cards)

        return {
                'total_cards': len(self.registered_cards),
                'matches_played': self.matches_played,
                'avg_rating': avg_rating,
                'platform_status': 'active'
                }
