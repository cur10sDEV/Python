import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_data = {row.letter: row.code for (index, row) in data.iterrows()}

name = input("Enter a name: ").upper()
result = [code for (letter, code) in nato_data.items() if letter in list(name)]
result2 = [nato_data[letter] for letter in name]
print(result2)






