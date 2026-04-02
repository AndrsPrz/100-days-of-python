"""
blackjack.py
============
A command-line Blackjack game played against the computer.
 
Rules implemented
-----------------
- The deck is represented as a list of card values; face cards (J, Q, K)
  all count as 10, and Aces start as 11 and automatically drop to 1 if
  the hand would otherwise bust.
- A natural Blackjack (21 in exactly 2 cards) is encoded as score 0 and
  beats any other hand instantly.
- The computer must draw until its score reaches 17 or above (standard
  soft-17 rule).
 
Dependencies
------------
- art  : third-party package used only to display the ASCII logo.
         Install with: pip install art
- random: standard library module used to draw random cards from the deck.
 
Usage
-----
    python blackjack.py
 
The game loops until the player answers 'n' to the "play again?" prompt.
"""
import random
from art import logo  

# ---------------------------------------------------------------------------
# Card and deck helpers
# ---------------------------------------------------------------------------
 
def deal_card(deck):
     """Return a randomly chosen card value from *deck*.
 
    The card is sampled with replacement, so the same value can appear
    multiple times (reflecting a real deck where several cards share a
    value, e.g. 10 for J/Q/K/10).
 
    Parameters
    ----------
    deck : list[int]
        The pool of available card values to draw from.
 
    Returns
    -------
    int
        A single card value chosen at random.
 
    Examples
    --------
    >>> deal_card([2, 3, 10, 11])
    10  # result will vary
    """
    return random.choice(deck)

# ---------------------------------------------------------------------------
# Score calculation
# ---------------------------------------------------------------------------
def calculate_score(cards):
 """Calculate the Blackjack score for a hand of cards.
 
    Special cases handled:
    - **Natural Blackjack**: a two-card hand that sums to 21 returns 0.
      The caller treats 0 as "Blackjack" (an unbeatable hand).
    - **Ace adjustment**: if the hand is over 21 and contains an Ace
      counted as 11, that Ace is downgraded to 1 to avoid busting
      whenever possible.
 
    Parameters
    ----------
    cards : list[int]
        The current hand as a list of integer card values.
        Aces are represented as 11; face cards as 10.
 
    Returns
    -------
    int
        - 0  → natural Blackjack (21 in 2 cards).
        - 1–21 → valid hand total.
        - >21  → bust (no Ace adjustment was possible).
 
    Notes
    -----
    Only the *first* Ace in the hand is adjusted. Hands with two Aces
    will still bust if both count as 11 and no further adjustment is
    made. This matches the simplified rules used in this game.
 
    Examples
    --------
    >>> calculate_score([11, 10])   # natural Blackjack
    0
    >>> calculate_score([11, 7, 5]) # Ace drops from 11 → 1 to avoid bust
    13
    >>> calculate_score([10, 9, 5]) # bust, no Ace to adjust
    24
    """
    # Natural Blackjack check (must come before Ace adjustment)
 
    if sum(cards) == 21 and len(cards) == 2:
        return 0
      # Ace adjustment: downgrade one Ace from 11 to 1 if the hand is bust
    
    if sum(cards) > 21 and 11 in cards:
        cards[cards.index(11)] = 1
 
    return sum(cards)
 
# ---------------------------------------------------------------------------
# End-of-round comparison
# ---------------------------------------------------------------------------

def compare(player_score, computer_score):
    """Compares final scores and prints the result."""
    if player_score == computer_score:
        print("Draw!")
    elif player_score == 0:
        print("Win with a Blackjack 😎")
    elif computer_score == 0:
        print("You lose. Opponent has Blackjack!")
    elif player_score > 21:
        print("You went over 21. You lose 😢")
    elif computer_score > 21:
        print("Opponent went over 21. You win 🥳")
    elif player_score > computer_score:
        print("You win 🥳")
    else:
        print("You lose 😢")
 
 
def play_game():
    print(logo)
 
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
 
    
    player_cards = [deal_card(cards), deal_card(cards)]
    computer_cards = [deal_card(cards), deal_card(cards)]
 
    game_over = False
 
    while not game_over:
 
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
 
        print(f"\n   Your cards: {player_cards}, current score: {player_score}")
        print(f"   Computer's first card: {computer_cards[0]}")
 
        
        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else:
            draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if draw_card == 'y':
                player_cards.append(deal_card(cards))
            else:
                game_over = True
 
    
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card(cards))
        computer_score = calculate_score(computer_cards)
 
   
    print(f"\n   Your final hand: {player_cards}, final score: {player_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    compare(player_score, computer_score)
 
 

while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play_game()
 
