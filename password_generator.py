import random

letters = ["a","b","c","d","e","f","g","h","i",
"j","k","l","m","n","o","p","q","r","s","t","u"
,"v","w","x","y","z"]
numbers = [0,1,2,3,4,5,6,7,8,9]
symbols = ["!","@","#","$","%","^","&","*","(",")"]

n_letters = int(input("Enter the number of letters you want?\n"))
n_numbers = int(input("Enter the number of numbers you want?\n"))
n_symbols = int(input("Enter the number of symbols you want?\n"))

password = []

for i in range(n_letters):
	password += random.choice(letters)

for i in range(n_numbers):
	password += str(random.choice(numbers))

for i in range(n_symbols):
	password += random.choice(symbols)

print(password)
random.shuffle(password)

generated_password = ""
for char in password:
	generated_password += "".join(char)

print(generated_password)