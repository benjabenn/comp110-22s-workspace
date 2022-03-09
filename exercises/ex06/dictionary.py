"""A variety of functions that work with dictionaries in Python."""


__author__ = "730518701"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts all of the keys and values of a dict, raises a KeyError for duplicate keys."""
    result: dict[str, str] = {}

    for key in input:
        # Raises a KeyError if an existingkey in the result is equal to the current value of the input that is about to become a key in the result.
        for existingkey in result:
            if existingkey == input[key]:
                raise KeyError
        result[input[key]] = key
    
    return result


def favorite_color(input: dict[str, str]) -> str:
    """Takes a dict of names and their favorite colors and returns the most common favorite color. Breaks ties with whichever color occurred first in the dict."""
    final_color: str = ""
    final_color_occurrence: int = 0

    for key in input:
        color_name: str = input[key]
        color_frequency: int = 0
        # This for...in loop creates a frequency of occurrence for each value
        for frequency_key in input:
            if color_name == input[frequency_key]:
                color_frequency += 1
        # Tests if the color frequency determined for the new value is greater then the older one, if so, the final values are set to that.
        if color_frequency > final_color_occurrence:
            final_color = color_name
            final_color_occurrence = color_frequency
    # No line of code necessary to break ties, as a new value after the first set one will never be assigned, therefore the first one always wins.
    return final_color


def count(input: list[str]) -> dict[str, int]:
    """From an inputted list, counts the number of times each item in that list occurs and stores the items as keys with number of occurrences as corresponding values."""
    result_dict: dict[str, int] = {}

    for key in input:
        if key in result_dict:
            result_dict[key] += 1
        else:
            result_dict[key] = 1

    return result_dict