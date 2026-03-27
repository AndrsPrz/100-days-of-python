import random
from art import logo  
 
 
def deal_card(deck):
    return random.choice(deck)
 
def calculate_score(cards)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if sum(cards) > 21 and 11 in cards:
        cards[cards.index(11)] = 1
 
    return sum(cards)
 
 
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
 
