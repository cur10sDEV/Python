import random
random_int = (random.randint(1, 4))
random_float = random.random() * 2
result = "nothing"

if random_int < 2: result = "Head"
else: result = "Tail"

print(result)