import secret_auction_art as saa
import os

# The objective is to write a program that will collect the names
# and bids of different people. The program should ask for each
# bidder's name and their bid individually.

# If there are other bidders, the screen should clear, so you can
# pass your phone to the next person. If there are no more bidders,
# then the program should display the name of the winner
# and their winning bid.

bids = {}
should_continue = True

def add_bid(name, bid):
    bids[name] = bid

while should_continue:
    print(saa.logo)
    name = input("What is your name?\n")
    bid = int(input("What's your bid?\n"))

    add_bid(name, bid)

    result = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if result == "yes":
        os.system('cls')
    else:
        should_continue = False

bids_keys = list(bids.keys())
bids_values = list(bids.values())
highest_bid_value = max(bids_values)
highest_bid_name = bids_keys[bids_values.index(highest_bid_value)]

print(f"The winner is {highest_bid_name} with a bid of ${highest_bid_value}.")