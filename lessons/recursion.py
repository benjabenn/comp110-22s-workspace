from __future__ import annotations

from typing import Optional


class Node:
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Init."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """String representation."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next.__str__()}"


def sum(node: Optional[Node]) -> int:
    if node is None:
        return 0
    else:
        return node.data + sum(node.next)


def count(node: Optional[Node], current_count: int = 0) -> int:
    if node is None:
        return current_count
    else:
        return count(node.next, current_count + 1)


head: Node = Node(3, None)
head = Node(2, head)
head = Node(1, head)
print(sum(head))
print(count(head))
print(head)


# def factorial(node: Node) -> int:
#     """Dumb factorial, but specifically of the values in the linked list lol."""
#     if node.next is None:
#         return node.data
#     else:
#         return node.data * factorial(node.next)


# i: int = 40
# head: Node = Node(41, None)
# while i > 0:
#     head = Node(i, head)
#     i -= 1

# print(factorial(head))