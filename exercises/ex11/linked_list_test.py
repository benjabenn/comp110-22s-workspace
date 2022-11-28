"""Tests for linked list utils."""

import pytest
from linked_list import Node, last, value_at, linkify, is_equal, scale, max

__author__ = 730518701


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_out_of_range() -> None:
    """Find value at an index out of range should raise an IndexError."""
    linked_list = Node(1, Node(2, Node(3, None)))
    with pytest.raises(IndexError):
        value_at(linked_list, 5)


def test_value_at_in_range() -> None:
    """Find value at an index in range should return indexed value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 2) == 3


def test_max_all_equal_values() -> None:
    """Makes sure the program returns a value properly when given all the same value in a linked list."""
    linked_list = Node(10, Node(10, Node(10, None)))
    assert max(linked_list) == 10


def test_max_target_in_middle() -> None:
    """Makes sure the program returns a value properly when given the largest value in the middle of a linked list."""
    linked_list = Node(40, Node(50, Node(20, None)))
    assert max(linked_list) == 50


def test_max_target_at_end() -> None:
    """Makes sure the program returns a value properly when given the largest value at the end of a linked list."""
    linked_list = Node(10, Node(30, Node(40, None)))
    assert max(linked_list) == 40


def test_max_other_test() -> None:
    """Additional test with 4 values, utilizing the linkify function."""
    assert max(linkify([10, 20, 40, 30])) == 40


def test_linkify_short_list() -> None:
    """Tests that linkify works with a short list of unique numbers."""
    input_list: list[int] = [1, 2, 4]
    linked_list = Node(1, Node(2, Node(4, None)))
    assert is_equal(linkify(input_list), linked_list) is True


def test_linkify_long_list() -> None:
    """Tests that linkify works with a longer list of unique numbers."""
    input_list: list[int] = [3, 2, 4, 9, 100, 43]
    linked_list = Node(3, Node(2, Node(4, Node(9, Node(100, Node(43, None))))))
    assert is_equal(linkify(input_list), linked_list) is True


def test_scale_one_node() -> None:
    """Tests that scale works with just one node in the linked list."""
    test_list: list[int] = [3]
    test_list_r: list[int] = [9] 
    assert is_equal(scale(linkify(test_list), 3), linkify(test_list_r)) is True


def test_scale_long_linked_list() -> None:
    """Tests that scale works with a longer linked list."""
    test_list: list[int] = [3, 8, 2, 40, 22]
    test_list_r: list[int] = [9, 24, 6, 120, 66] 
    assert is_equal(scale(linkify(test_list), 3), linkify(test_list_r)) is True