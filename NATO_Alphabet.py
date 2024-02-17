import pandas
phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_alphabet_dict = {row.letter: row.code for (index, row) in phonetic_alphabet.iterrows()}

word = input("Type a word: ").upper()
letter_list = [phonetic_alphabet_dict[letter] for letter in word]
print(letter_list)

# phonetic_name = [name for name in phonetic_alphabet_dict if letter_list in phonetic_alphabet_dict]
# print(phonetic_name)
