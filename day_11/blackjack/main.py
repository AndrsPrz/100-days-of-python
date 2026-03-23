import random
start = None
start = input(f"Do you want to play a game of blackjack? Type 'y' or 'n': ")
if start == 'y':
    start = True
while start == True:
    print("Welcome to the game! SIMBOL")
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_card = random.sample(cards, 2)
    player_total_score = sum(player_card)
    print(f"your cards: {player_card}, current score: {player_total_score}")
    computer_card = random.sample(cards, 2)
    print(f"Computer's first card: {computer_card[0]}")
    player_to_additional_card = input(f"Type 'y' to to get another card, type 'n' to pass: ")
    while player_to_additional_card == 'y':
        player_new_card = random.sample(cards, 1)
        player_card.extend(player_new_card)
        player_total_score = sum(player_card)
        #to add a funtion
        print(f"your cards: {player_card}, current score: {player_total_score}")
        print(f"Computer's first card: {computer_card[0]}")
        player_to_additional_card = input(f"Type 'y' to to get another card, type 'n' to pass: ")
        if player_total_score > 21:
            print(f"Your final hand: {player_card}, final score: {player_total_score}")
            print(f"Computer's final hand: {computer_card}, final score: {sum(player_total_score)}")
            print(f"You went over. You lose :(")
            #to fix the final and while loop.
            player_to_additional_card = 'n'
            start = False

            break

        elif player_to_additional_card == 'n':
            print(f"Your final hand: {player_card}, final score: {player_total_score}")
            break

    start = False