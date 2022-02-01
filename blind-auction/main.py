import os
import art

def clear():
	os.system("cls" if os.name == "nt" else "clear")

print(art.logo)
print("Welcome to the secret auction program.\n")

max_value = None
winner = None
is_auction_live = "yes"
bidder_list = []
while is_auction_live == "yes":
	name = input("What is your name?: ")
	bid = int(input("What's your bid?: $"))
	bidder_info = {
	"name": name,
	"bid": bid,
	}
	bidder_list.append(bidder_info)

	for i in range(1, len(bidder_list)):
		current_bid = bidder_list[i]["bid"]
		prev_bid = bidder_list[i-1]["bid"]
		if current_bid > prev_bid: max_value = current_bid
		else: max_value = prev_bid

	for bidder in bidder_list:
		if bidder["bid"] == max_value:
			winner = bidder["name"]
			break
	is_auction_live = input("Are there any other bidders? Type 'yes' or 'no'. ")
	if len(bidder_list) == 1:
		max_value = bid
		winner = name

	clear()
print(f"The winner is {winner} with a bid of ${max_value}")