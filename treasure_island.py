def treasure_hunt():
	first = input("Type left or right\n").lower()
	if (first == "right"): print("Game over")
	else:
		second = input("Type swim or wait\n").lower()
		if (second == "swim"): print("Game over")
		else:
			third = input("Which door? red or blue or yellow?\n").lower()
			if (third == "yellow"): print("You win")
			else: print("Game over")

treasure_hunt()