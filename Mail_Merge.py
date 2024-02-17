PLACE_HOLDER = "[name]"

names = open("input/invited_names.txt")
names_list = names.readlines()
with open("input/starting_letter.txt") as letter_contents:
    letter = letter_contents.read()


for name in names_list:
    new_name = name.strip()
    new_letter = letter.replace(PLACE_HOLDER, new_name)
    print(new_letter)
    with open(f"{new_name}.txt", "w" ) as file:
        file.write(new_letter)

