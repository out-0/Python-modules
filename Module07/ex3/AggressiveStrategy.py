from typing import List
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard


class AggressiveStrategy:
    """This strategy is relay on using the cards that cost
    less than 5 mana point.
    """

    # Execute actions of strategy.
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """
        Execute the hand with that strategy used.

        Argument => Hand

        Check all the hand and play the card just if it cost
        less than 5 mana

        Return report of the actions used
        """

        # Define the result info
        cards_played: List[Card] = []
        mana_used: int = 0
        damage_dealt: int = 0

        #
        # Copy the enemies to avoid friendly fire when added
        # your card to the battlefield, so at the attack u attack
        # the enemies list but inside the play it will add to battlefield
        # [:] is to create a new list not
        # just a reference that will updated also.
        enemies: List[Card] = battlefield[:]

        # Just to demonstrate.
        available_mana: int = 20
        is_playable: bool = True
        game_state = {
                      'is_playable': is_playable,
                      'available_mana': available_mana,
                      'battlefield': battlefield
                      }

        try:
            # Check the hand in fill the info
            for card in hand:
                if card.cost < 5:
                    card.play(game_state)  # => Play card
                    cards_played.append(card.name)  # => Add to played
                    mana_used += card.cost

                    # if its Creature so he can fight
                    if isinstance(card, CreatureCard):
                        damage_dealt += card.attack

                        # Check targets list is not empty
                        if enemies:
                            for enemy in enemies:
                                card.attack_target(enemy)
                        # If targets empty, attack the player.
                        else:
                            print(f"{card.name} attack the fucking "
                                  "player directly ⚡️")

                    else:
                        damage_dealt += card.damage
                        if enemies:
                            for enemy in enemies:
                                enemy.health -= card.damage

                        # If targets empty, attack the player.
                        else:
                            print(f"{card.name} attack the fucking "
                                  "player directly ⚡️")

        except Exception as e:
            print("Error Detected: Something happen "
                  "while executing strategy actions")
            print(e)
            return {}

        # Map and extract names from objects.
        enemies = [enemy.name for enemy in enemies]
        return {
                'cards_played': cards_played,
                'mana_used': mana_used,
                'targets_attacked': enemies,
                'damage_dealt': damage_dealt
                }

    def get_strategy_name(self) -> str:
        """Just return the strategy name"""
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        pass
