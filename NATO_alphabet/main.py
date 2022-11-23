import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")


# TODO 1. Create a dictionary in this format:
NATO_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_name = input("Enter a word. ").upper()
users_code_words_faster = [NATO_dict[letter] for letter in user_name]
print(users_code_words_faster)
