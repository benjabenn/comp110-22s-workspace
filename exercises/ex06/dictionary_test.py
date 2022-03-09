"""Tests for that variety of functions that work with dictionaries in Python, one edge case and two use cases each."""


__author__ = "730518701"

from dictionary import invert, favorite_color, count


def test_invert_empty() -> None:
    """Tests that the empty dict inputted returns the empty dict."""
    xs: dict[str, str] = {}
    assert invert(xs) == {}


def test_invert_short() -> None:
    """Tests that a dict of 1 key and 1 value is inverted."""
    xs: dict[str, str] = {'Bingo': 'Bongo'}
    assert invert(xs) == {'Bongo': 'Bingo'}


def test_invert_many() -> None:
    """Tests that a long list is inverted properly."""
    xs: dict[str, str] = {'The': 'Quick', 'Red': 'Fox', 'Jumped': 'Over', 'A': 'Lazy', 'Brown': 'Dog'}
    assert invert(xs) == {'Quick': 'The', 'Fox': 'Red', 'Over': 'Jumped', 'Lazy': 'A', 'Dog': 'Brown'}


def test_favorite_color_one() -> None:
    """One dictionary entry with one favorite color should return that favorite color in this test."""
    xs: dict[str, str] = {'Mack': 'yellow'}
    assert favorite_color(xs) == "yellow"


def test_favorite_color_tie() -> None:
    """A tie in number of occurrences should be resolved by which item came first in this test."""
    xs: dict[str, str] = {'Mack': 'yellow', 'Jordana': 'yellow', 'Noble': 'green', 'Brooks': 'green', 'Jeremy': 'blue'}
    assert favorite_color(xs) == "yellow"


def test_favorite_color_many() -> None:
    """Tests that a dict of many keys and values returns the correct (most frequent) color."""
    xs: dict[str, str] = {'Mack': 'yellow', 'Jordana': 'yellow', 'Noble': 'green', 'Brooks': 'green', 'Jeremy': 'blue', 'John': 'green', 'Jared': 'red'}
    assert favorite_color(xs) == "green"


def test_count_empty() -> None:
    """Tests that the empty list inputted returns the empty dict."""
    xs: list[str] = []
    assert count(xs) == {}


def test_count_tie() -> None:
    """Makes sure multiple keys in the dict can count to the same value."""
    xs: list[str] = ["black", "black", "bird", "bird", "singing", "singing"]
    assert count(xs) == {'black': 2, 'bird': 2, 'singing': 2}


def test_count_variety() -> None:
    """Given a list of a variety of repeating str values, should return appropriate counts for all."""
    xs: list[str] = ["landmine", "landmine", "has", "taken", "my", "arms", "taken", "my", "legs", "taken", "my", "soul", "left", "me", "with", "life", "in", "hell", "hell", "hell", "hell"]
    assert count(xs) == {'landmine': 2, 'has': 1, 'taken': 3, 'my': 3, 'arms': 1, 'legs': 1, 'soul': 1, 'left': 1, 'me': 1, 'with': 1, 'life': 1, 'in': 1, 'hell': 4}