import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")


# TODO 1. Create a dictionary in this format:
NATO_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    user_name = input("Enter a word. ").upper()
    try:
        users_code_words_faster = [NATO_dict[letter] for letter in user_name]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(users_code_words_faster)

generate_phonetic()
