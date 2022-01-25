n = int(input("Enter the number you want to add upto\n"))
total = 0
even_sum = 0
odd_sum = 0
for i in range(n+1):
	total += i
	# sum of only even numbers
	if(i % 2 == 0):
		even_sum += i
	# sum of only odd numbers
	if(not(i%2 == 0)):
		odd_sum += i
print(f"Sum of numbers upto and including 100 is {total}")
print(f"Sum of even numbers upto and including 100 is {even_sum}")
print(f"Sum of odd numbers upto 100 is {odd_sum}")