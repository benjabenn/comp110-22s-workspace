"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730518701"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    elif head.next is None:
        return head.data
    else:
        return last(head.next)


def value_at(head: Optional[Node], index: int) -> int:
    """Finds the value of a linked list at a given index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    elif index == 0:
        return head.data
    else:
        return value_at(head.next, index - 1)


# def max(head: Optional[Node]) -> Optional[int]:  # STILL NOT RIGHT AHHHHHHHHHHHHHHHHHHHHHHHHHHHH
#     """Returns the maximum value found in a linked list."""
#     if head is None:
#         raise ValueError("Cannot call max with None")
#     elif head.next is None or value_at(head.next, 0) <= head.data:
#         return head.data
#     elif value_at(head.next, 0) >= head.data:
#         return max(head.next)
#     else:
#         raise Exception("Something bad happened.")

def max(head: Optional[Node]) -> int:
    """Returns the max value in a given linked list."""
    if head is None:
        raise ValueError("Cannot call max with None.")
    else:
        if head.next is None:
            return head.data
        else:
            next_max: int = max(head.next)
            if head.data < next_max:
                return next_max
            else:
                return head.data


def linkify(items: list[int]) -> Optional[Node]:
    """Turns a list of ints into a linked list."""
    if items == []:
        return None
    else:
        return Node(items[0], linkify(items[1:]))


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """Scales every value in a linked list by the factor."""
    if head is None:
        return None
    else:
        return Node(head.data * factor, scale(head.next, factor))


def main():
    print(max(linkify([10, 0, 40, 30])))


if __name__ == "__main__":
    main()