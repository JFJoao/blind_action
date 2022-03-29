from replit import clear

def highest_bid(bidding_record):
    high_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
    if bid_amount > high_bid:
        high_bid = bid_amount
        winner = bidder
    print(f"The winner is {winner} with bid of {high_bid}")

end_of_bids = False
bid_list = {}

while not end_of_bids:
    name = input("What's your name?\n")
    price = int(input("What's your bid ?\n"))
    bid_list[name] = price
    more_people = input("There's more people? yes or no.\n") .lower()
    if more_people == "no":
        highest_bid(bid_list)
        end_of_bids = True
    elif more_people == "yes":
        clear()


