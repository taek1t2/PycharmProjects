# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo
print(logo)

def finding_highest_bidder(bid_dict):
    winner = ""
    max_bid = 0
    for any_bidder in bid_dict:
        bid_amount = bid_dict[any_bidder]
        if bid_amount > max_bid:
            max_bid = bid_amount
            winner = any_bidder
    print(f"The highest bidder is {winner} with a bid of ${max_bid}.")

all_bidders = {}

continue_to_bid = True
while continue_to_bid:
    bidder = input("The name of the bidder: ")
    price_bid = int(input("What is your bid?: $"))
    all_bidders[bidder] = price_bid
    any_other_bidder = input("Are there any other bidders? (y/n) \n").lower()
    print("\n" * 100)
    if any_other_bidder == "n":
        continue_to_bid = False
        finding_highest_bidder(all_bidders)
    elif any_other_bidder == "y":
        continue_to_bid = True



