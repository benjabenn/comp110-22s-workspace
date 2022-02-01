"""EX02 - A game of Wordle where the player has one shot, one opportunity, and they must capture it!"""

__author__ = "730518701"

secret_word: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

player_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
while len(player_guess) != len(secret_word):
    player_guess: str = input(f"That was not {len(secret_word)} letters! Try again: ")

# 
idx: int = 0
guess_result: str = ""

while idx < len(secret_word):
    if player_guess[idx] == secret_word[idx]:
        guess_result += GREEN_BOX
    else:
        character_exists: bool = False
        alt_idx: int = 0
        while not character_exists and alt_idx < len(secret_word):
            if secret_word[alt_idx] == player_guess[idx]:
                character_exists = True
            else:
                alt_idx += 1
        if character_exists:
            guess_result += YELLOW_BOX
        else:
            guess_result += WHITE_BOX
    idx += 1

# 
print(guess_result)

if player_guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")