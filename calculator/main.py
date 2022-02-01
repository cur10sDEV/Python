import os
from art import logo

print(logo)

to_continue = True
go_ahead = "n"
num1 = 0
result = None
error = "You entered an invalid input, Please restart the program"

while to_continue:
	if go_ahead == "n":
		num1 = float(input("Enter the first number: "))
	operation = input('''
		+
		-
		*
		/
		Pick an Operation: ''')
	num2 = float(input("Enter second number: "))

	if operation == "+": result = round(num1 + num2,2)
	elif operation == "-": result = round(num1 - num2,2)
	elif operation == "*": result = round(num1 * num2,2)
	elif operation == "/": result = round(num1 / num2,2)
	else: print(error)
	
	print(f"{num1} {operation} {num2} = {result}")
	
	go_ahead = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation or type 'e' to exit: ")
	if go_ahead == "n": os.system("cls" if os.name == "nt" else "clear")
	elif go_ahead == "e":
		to_continue = False
		print("Thanks for using me")
	elif go_ahead == "y": num1 = result
	else: print(error)
