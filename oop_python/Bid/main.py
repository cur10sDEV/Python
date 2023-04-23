from os import system
print("Welcome to the secret auction Program.")
to_move_forward = True
bidders = []
high = {"name": "", "amount": 0}

while to_move_forward:
    name = input("What is your name?: ")
    bid_amount = float(input("What's your bid?: $"))
    conti_nue = input("\nAre there any other bidders? Type 'yes' or 'no'.\n")
    bidder = {"name": name, "amount": bid_amount}
    bidders.append(bidder)
    if conti_nue == "no":
        for bidder in bidders:
            if high["amount"] < bidder["amount"]:
                high["amount"] = bidder["amount"]
                high["name"] = bidder["name"]
        to_move_forward = False
        print(f'''Winner is {high["name"]}''')
        print(f"Winning Amount: ${high['amount']}")
    elif conti_nue == "yes":
        continue
        system("clear")
    else:
        print("You messed up")
        break