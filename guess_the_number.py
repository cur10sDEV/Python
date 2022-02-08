import random
logo = """
 dP""b8 88   88 888888 .dP"Y8 .dP"Y8   888888 88  88 888888   88b 88 88   88 8b    d8 88""Yb 888888 88""Yb 
dP   `" 88   88 88__   `Ybo." `Ybo."     88   88  88 88__     88Yb88 88   88 88b  d88 88__dP 88__   88__dP 
Yb  "88 Y8   8P 88""   o.`Y8b o.`Y8b     88   888888 88""     88 Y88 Y8   8P 88YbdP88 88""Yb 88""   88"Yb  
 YboodP `YbodP' 888888 8bodP' 8bodP'     88   88  88 888888   88  Y8 `YbodP' 88 YY 88 88oodP 888888 88  Yb 
 """
print("Welcome to the Number Guessing Game!")
print(logo)
print("I'm thinking of a number between 1 and 100.")
attempts = 10
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if level == "hard": attempts -= 5
numbers = []
for i in range(1,101):
	numbers.append(i)
selected_no = random.choice(numbers)
win = False
while win == False:
	while attempts > 0:
		print(f"\nYou have {attempts} attempts remaining to guess the number.")
		guess = int(input("Make a guess: "))
		if guess == selected_no:
			print("\nYou Win :-)")
			win = True
			attempts = 0
		elif guess > selected_no:
			print("Too high")
			if attempts == 1: print("\nGame Over :-(")
			else: print("Guess again")
			attempts -= 1
		elif guess < selected_no:
			print("Too low")
			if attempts == 1: print("\nGame Over :-(")
			else: print("Guess again")
			attempts -= 1
	if attempts <= 0:
		break