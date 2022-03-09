"""Tests for that variety of functions that work with dictionaries in Python, one edge case and two use cases each."""


__author__ = "730518701"

from dictionary import invert


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


