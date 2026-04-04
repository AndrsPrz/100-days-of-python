import os
from art import logo

# Display the ASCII art logo at the start of the program
print(logo)

def ask_for_bid(bids):
    """
    Prompt the current bidder for their name and bid amount,
    then store the result in the shared bids dictionary.

    Args:
        bids (dict): A dictionary mapping bidder names to their bid amounts.
    """
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[name] = bid


def find_winner(bids):
    """
    Determine and announce the winner of the auction.

    Iterates through all entries in the bids dictionary,
    finds the highest bid, and prints the winner's name and amount.

    Args:
        bids (dict): A dictionary mapping bidder names to their bid amounts.
    """
    highest_bid = 0
    winner = ""

    for name in bids:
        if bids[name] > highest_bid:
            highest_bid = bids[name]
            winner = name

    print(f"The winner is {winner} with a bid of ${highest_bid}")


# Dictionary to store all bids in the format { name: bid_amount }
bids = {}
another_bidder = "yes"

# Keep collecting bids until no more bidders remain
while another_bidder == "yes":
    ask_for_bid(bids)
    another_bidder = input("Are there any other bidders? Type 'yes' or 'no': ")
    os.system("clear")  # Clear the screen so the next bidder can't see previous bids

# Once all bids are in, find and announce the winner
if another_bidder == "no":
    find_winner(bids)