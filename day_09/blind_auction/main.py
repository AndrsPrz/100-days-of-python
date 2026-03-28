import os
from art import logo

print(logo)

def ask_for_bid(bids):
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[name] = bid 

def find_winner(bids):
    highest_bid = 0
    winner = ""
    for name in bids:
        if bids[name] > highest_bid:
            highest_bid = bids[name]
            winner = name
    print(f"The winner is {winner} with a bid of ${highest_bid}")

bids = {}
another_bidder = 'yes'

while another_bidder == 'yes':
    ask_for_bid(bids)
    another_bidder = input("Are there any other bidders? Type 'yes' or 'no': ")
    os.system('clear')

if another_bidder == 'no':
    find_winner(bids)