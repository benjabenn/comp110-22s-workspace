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


def favorite_color(input: dict[str, str]) -> dict[str, int]:
    """Takes a dict of names and their favorite colors and returns the most common favorite color. Breaks ties with whichever color occurred first in the dict."""
    results_dict: dict[str, int] = dict()

    for key in input:
        for existingkey in results_dict:
            if input[key] in results_dict:
                results_dict[input[key]] += 1
            else:
                results_dict[input[key]] = 1
    
    return results_dict


print(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}))