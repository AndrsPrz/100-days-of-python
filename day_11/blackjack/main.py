import random
start = None
start = input(f"Do you want to play a game of blackjack? Type 'y' or 'n': ")
if start == 'y':
    start = True
while start == True:
    print("Welcome to the game! SIMBOL")
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_card = random.sample(cards, 2)
    print(f"your cards: {player_card}, current score: {player_card[0]+player_card[1]}")
    print(player_card)
    start = False