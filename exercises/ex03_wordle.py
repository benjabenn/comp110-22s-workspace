"""An extension of one shot wordle into 6 turns using function definitions."""

__author__ = "730518701"


def contains_char(string_searched: str, character_search: str) -> bool:
    """A function to find if 'character_search' is found at all within 'string_searched'."""
    assert len(character_search) == 1
    char_search_idx: int = 0
    character_presence: bool = False
    
    while char_search_idx < len(string_searched):
        if character_search == string_searched[char_search_idx]:
            character_presence = True
        char_search_idx += 1

    return character_presence


def emojified(user_guess: str, secret: str) -> str:
    """Produce a string of emoji color coded to display white, yellow, and green for incorrect, mispositioned, and correct guesses respectively."""
    assert len(user_guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    emoji_result: str = ""

    str_search_idx: int = 0
    while str_search_idx < len(secret):
        # First if statement checks for matching positions, one character == one character
        if contains_char(secret[str_search_idx], user_guess[str_search_idx]):
            emoji_result += GREEN_BOX
        # Elif statement uses the whole word as the string that is searched, finds if it is anywhere in the word
        elif contains_char(secret, user_guess[str_search_idx]):
            emoji_result += YELLOW_BOX
        # Else, the contains_char function is entirely false, and the letter is not present
        else:
            emoji_result += WHITE_BOX
        str_search_idx += 1
    return emoji_result


def input_guess(expected_length: int) -> str:
    """Prompt user for str guess until it is of expected length."""
    user_input: str = input(f'Enter a {expected_length} character word: ')
    while len(user_input) != expected_length:
        user_input = input(f'That wasn\'t {expected_length} chars! Try again: ')

    return user_input


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn_idx: int = 1
    game_length: int = 6
    secret_word: str = "codes"
    secret_length: int = len(secret_word)
    won_game: bool = False
    # While some of the variables declared in main could have been named the same as the ones declared
    # in other functions, in order to not confuse variables, small naming changes were made to identify
    # which ones were used with finality and the main function in mind (i.e. user_input vs final_user_input)

    while turn_idx <= game_length and not won_game:
        print(f'=== Turn {turn_idx}/{game_length} ===')
        # Creates a string that is the final user input that has gone through the process of length correction through input_guess
        final_user_input: str = input_guess(secret_length)
        # Gives the user their emojified hints/results
        print(emojified(final_user_input, secret_word))
        if final_user_input == secret_word:
            won_game = True
        # Must use an else here, otherwise the turn count when the game is won will be inaccurate
        else:
            turn_idx += 1
    
    if won_game:
        print(f'You won in {turn_idx}/{game_length} turns!')
    else:
        print(f'X/{game_length} - Sorry, try again tomorrow!')


if __name__ == "__main__":
    main()