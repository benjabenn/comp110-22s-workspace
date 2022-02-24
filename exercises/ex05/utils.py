"""Implementation of some list-related skeleton functions."""


__author__ = "730518701"


def only_evens(full_list: list[int]) -> list[int]:
    """Input is a list of integers, removes all odd integers found within the list and returns the result."""
    i: int = 0

    while i < len(full_list):
        if full_list[i] % 2 == 1:
            full_list.pop(i)
        else:
            i += 1

    return full_list


def sub(full_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Takes a list of ints and returns a subset of that list between the start and end index, not including the end."""
    i: int = 0

    while i < len(full_list):
        if i < start_index:
            full_list.pop(i)
        elif i < end_index:
            i += 1
        else:
            full_list.pop(i)

    return full_list


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Takes both inputted list and combines them so all of the elements of the first list are followed by all of the elements of the second list."""
    i: int = 0
    full_list: list[int] = list()

    while i < len(first_list):
        full_list.append(first_list[i])
        i += 1
    
    i = 0

    while i < len(second_list):
        full_list.append(second_list[i])
        i += 1

    return full_list