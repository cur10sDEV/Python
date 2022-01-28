import random
import hangman_words
import hangman_art
import os

def clear():
	os.system("cls" if os.name == "nt" else "clear")

logo = hangman_art.logo
stages = hangman_art.stages
word_list = hangman_words.word_list

chosen_word = random.choice(word_list)
word = []
final_word = []

print(logo)

for letter in chosen_word:
	word += letter
	final_word += "_"

lives = 7

def displayfunc(final_word):
	display = ""
	for char in final_word:
		display += "".join(char)
	return display

while lives > 0:
	if "_" in final_word:
		guess = input("Enter letter: ")
		clear()
		for i in range(len(word)):
			if guess == word[i]:
				final_word[i] = guess
		if guess not in word:
			lives -= 1
			print("\nYou typed letter dosent fit in the chosen word. you lose a life")
			print(f"\n{stages[lives]}\n")
		print(f"\n{displayfunc(final_word)}\n")
	elif "_" not in final_word:
		print("\nYOu win\n")
		break
if lives == 0 and "_" in final_word:
	print("\nGame Over, You Lose\n")