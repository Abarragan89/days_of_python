# Get all names from the file and place.
with open("./Input/Names/invited_names.txt",
          mode="r") as name_data:
    names = name_data.readlines()

for name in names:
    name = name.strip()
    with open("./Input/Letters/starting_letter.txt", mode="r") as template:
        letter = template.readlines()
        letter[0] = letter[0].replace("[name]", name)
        print(letter)
        custom_letter = "".join(letter)
    file_path = f"./Output/ReadyToSend/{name}_invite.txt"
    with open(file_path, "w") as new_letter:
        new_letter.write(custom_letter)


