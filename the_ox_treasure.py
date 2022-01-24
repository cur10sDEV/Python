##### THE O-X GAME
print("\n###################################\n")
row_1 = ["_","_","_"]
row_2 = ["_","_","_"]
row_3 = ["_","_","_"]

game_map = [row_1, row_2, row_3]
print(f"""
	{row_1}
	{row_2}
	{row_3}
	""")

print("""
	#### Game Rules ####
	Use spaces in between position
	example: column row i.e., 2 3
	""")

position = input("Where do you want to put the treasure?\n").split(' ')
game_map[int(position[1]) - 1][int(position[0]) - 1] = "X"

print(f"""\n
	{row_1}
	{row_2}
	{row_3}
	\n""")
print("###################################")