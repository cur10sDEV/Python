####### Who's going to buy the meal today???...
import random
names = input("Enter the names of the contenders\n")
contenders = names.split(", ")

index = random.randint(0, len(contenders)-1)
random_name = contenders[index]
## OR ##
#random_name = random.choice(contenders)

print(f"{random_name} is going to buy the meal today!")