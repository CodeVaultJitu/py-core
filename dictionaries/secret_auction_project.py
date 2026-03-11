import art

print(art.logo)
print("Welcome message: Secret auction program starting.")

def highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_price = bidding_dictionary[bidder]
        if bid_price > highest_bid:
            highest_bid = bid_price
            winner = bidder

    print(f"The winner is {winner} with bid amount ${highest_bid}")


auction = {}
bidders = True

while bidders:
    name = input("Enter your bidder name.")
    price = int(input("What's your bid?: $"))
    auction[name] = price

    more_bidders = input("Are there more bidders? Answer 'yes' to continue adding bids, or 'no' to finish.").lower()

    if more_bidders == "no":
        bidders = False
        highest_bidder(auction)
    elif more_bidders == "yes":
        print("\n" * 10)