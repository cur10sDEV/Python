def love_calculator():
	name_1 = input("Enter your name: ").lower()
	name_2 = input("Enter your crush/lover name: ").lower()

	combined_name = name_1+name_2

	total_1 = combined_name.count("t") + combined_name.count("r") + combined_name.count("u") + combined_name.count("e")
	total_2 = combined_name.count("l") + combined_name.count("o") + combined_name.count("v") + combined_name.count("e")
	
	score = int(f"{total_1}{total_2}")

	if (score <= 10 or score >= 90): print(f"Your score is {score}, you go together like coke and mentos.")
	elif (40 <= score <= 50): print(f"Your score is {score}, you are alright together")
	else: print(f"Your score is {score}")

love_calculator()