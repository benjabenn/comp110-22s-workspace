"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730518701"

full_5_character_word: str = input("Enter a 5-character word: ")
if len(full_5_character_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

single_character: str = input("Enter a single character: ")
if len(single_character) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + single_character + " in " + full_5_character_word)

matching_characters: int = 0

if single_character == full_5_character_word[0]:
    print(single_character + " found at index 0")
    matching_characters = matching_characters + 1

if single_character == full_5_character_word[1]:
    print(single_character + " found at index 1")
    matching_characters = matching_characters + 1

if single_character == full_5_character_word[2]:
    print(single_character + " found at index 2")
    matching_characters = matching_characters + 1

if single_character == full_5_character_word[3]:
    print(single_character + " found at index 3")
    matching_characters = matching_characters + 1

if single_character == full_5_character_word[4]:
    print(single_character + " found at index 4")
    matching_characters = matching_characters + 1

if matching_characters == 0:
    print("No instances of " + single_character + " found in " + full_5_character_word)
else:
    if matching_characters == 1:
        print(str(matching_characters) + " instance of " + single_character + " found in " + full_5_character_word)
    else:
        print(str(matching_characters) + " instances of " + single_character + " found in " + full_5_character_word)