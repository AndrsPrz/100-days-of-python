"""
Number Guessing Game
====================
A terminal-based number guessing game where the player tries to guess
a randomly chosen number between 1 and 100. Supports two difficulty
levels with a configurable number of attempts.
 
Author: Andrés Pérez (AndrsPrz)
Day:    12 — 100 Days of Code: The Complete Python Pro Bootcamp (Angela Yu)
"""
 
import random
import art
 
 
# ---------------------------------------------------------------------------
# Core logic
# ---------------------------------------------------------------------------
 
def logic(difficulty: str, computer_number: int) -> None:
    """Run a single round of the guessing game.
 
    Manages the guess-and-feedback loop for one round. The player is given
    a fixed number of attempts depending on the chosen difficulty level. Each
    guess is validated to ensure it is an integer; non-integer inputs prompt
    the player to try again without consuming an attempt.
 
    Args:
        difficulty (str): Difficulty level selected by the player.
            - 'easy'  → 10 attempts
            - 'hard'  → 5 attempts
        computer_number (int): The secret number the player must guess,
            randomly chosen in the range [1, 100].
 
    Returns:
        None
    """
    # Assign attempts according to difficulty
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
 
    # Main guessing loop
    while attempts > 0:
        print(f"\nYou have {attempts} attempt(s) remaining to guess the number.")
        guess = input("Make a guess: ")
 
        # Validate that the input is an integer
        try:
            guess_number = int(guess)
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 100.")
            continue  # Do not consume an attempt for invalid input
 
        attempts -= 1
 
        # Evaluate the guess
        if guess_number > computer_number:
            print("Too high!")
        elif guess_number < computer_number:
            print("Too low!")
        elif guess_number == computer_number:
            print(f"You got it! The answer was {computer_number}.")
            break  # Exit the loop immediately on a correct guess
 
        # Inform the player about remaining attempts or loss
        if attempts == 0:
            print(f"\nYou've run out of attempts. The number was {computer_number}. You lose!")
        else:
            print("Guess again.")
 
# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
 
def main() -> None:
    """Launch and control the main game session.
 
    Displays the welcome screen once, then runs the game loop. After each
    round the player is asked whether they want to play again. The loop
    continues as long as the player responds with 'yes'.
    """
    # Display logo and welcome message
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
 
    # Main play-again loop
    to_play = 'yes'
    while to_play == 'yes':
 
        # Generate a new secret number for each round
        print("\nI'm thinking of a number between 1 and 100.")
        computer_number = random.randint(1, 100)
 
        # Ask the player to choose a difficulty level
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
        while difficulty not in ('easy', 'hard'):
            difficulty = input("Invalid choice. Please type 'easy' or 'hard': ").strip().lower()
 
        # Run the game logic for this round
        logic(difficulty, computer_number)
 
        # Ask whether the player wants to play again
        to_play = input("\nDo you want to play again? Type 'yes' or 'no': ").strip().lower()
 
    print("\nThanks for playing. See you next time!")
 
 
if __name__ == "__main__":
    main()
 
