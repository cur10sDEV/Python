def ticket():
	height = int(input("Enter your height (in cm): "))
	ticket = 0

	if (height >= 120):
		age = int(input("Enter your age: "))

		if (age < 12):
			ticket = 5
		elif (age <= 18):
			ticket = 7
		elif (age > 18):
			ticket = 12
			if (45 < age < 55):
				ticket = 0
				print("Everything is going to be ok!, This ride is on us.")

		photos = input("Do you want to click pictures? 'Y' or 'N'")
		if (photos == "Y" and not 45 < age < 55): ticket += 3

		print(f"You have to pay ${ticket}")

	else: print("Sorry you have to grow taller!")

ticket()