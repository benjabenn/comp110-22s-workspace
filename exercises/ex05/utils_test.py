"""Unit tests to test the functions in the utility module, using one edge case and two use cases for each function."""


__author__ = "730518701"

from utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Tests that the empty list is returned when it is inputted."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_many_evens() -> None:
    """Tests that the function removes only the odd ints when given many even ints."""
    xs: list[int] = [2, 4, 6, 8, 9, 10, 11]
    assert only_evens(xs) == [2, 4, 6, 8, 10]


def test_only_evens_many_odds() -> None:
    """Test for many odd inputs, the function should return the few evens."""
    xs: list[int] = [1, 5, 6, 121, 125, 18, 99]
    assert only_evens(xs) == [6, 18]


def test_sub_empty() -> None:
    """Tests to make sure the empty list is returned when it is inputted with a starting index greater than the length and an ending index less than 0."""
    xs: list[int] = []
    assert sub(xs, 2, -1) == []


def test_sub_included_subset() -> None:
    """Tests for the proper return of a short subset of the given list, starting from the beginning with a negative start index."""
    xs: list[int] = [22, 44, 66, 33, 11]
    assert sub(xs, 1, 3) == [44, 66]


def test_sub_short_subset() -> None:
    """Tests for the proper return of a short subset of the given list, starting from the beginning with a negative start index."""
    xs: list[int] = [22, 44, 66, 33, 11]
    assert sub(xs, -1, 2) == [22, 44]


def test_sub_full_subset() -> None:
    """Tests to return the whole list, beginning with 0 as the start index and an arbitrarily large number as the end index."""
    xs: list[int] = [88, 99, 23, 47, 26]
    assert sub(xs, 0, 99) == [88, 99, 23, 47, 26]


def test_concat_empty() -> None:
    """Tests to return the empty list when it is inputted."""
    xs: list[int] = []
    xs1: list[int] = []
    assert concat(xs, xs1) == []


def test_concat_single_items() -> None:
    """Tests to make sure lists of single items can be concatenated properly by this function."""
    xs: list[int] = [1]
    xs1: list[int] = [33]
    assert concat(xs, xs1) == [1, 33]


def test_concat_large_lists() -> None:
    """Tests to make sure large lists are concatenated in order when combined by this function."""
    xs: list[int] = [1, 3, 5, 0, 560]
    xs1: list[int] = [789, 2, 1, 88, 90]
    assert concat(xs, xs1) == [1, 3, 5, 0, 560, 789, 2, 1, 88, 90]