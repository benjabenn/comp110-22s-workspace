"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = 730518701


class Simpy:
    """A simp for NumPy."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Initializes the values of Simpy in list form."""
        self.values = values

    def __str__(self) -> str:
        """Returns a str for Simpy with the form 'Simpy(...)'."""
        return f"Simpy({self.values})"

    def fill(self, value: float, occurrences: int) -> None:
        """Mutating function that fills self.values with a value occurrences number of times."""
        self.values = []
        i: int = 0
        while i < occurrences:
            self.values.append(value)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills self.values with values ranging from start to stop, separated by step, not including stop."""
        result: list[float] = []
        length: int = int((stop - start) // step)
        assert step != 0.0  # Probably not necessary because step is the denominator of int division in the previous line, will raise error either way.

        i: int = 0
        while i < length:
            result.append(start + (step * i))
            i += 1

        self.values = result

    def sum(self) -> float:
        """Adds up the list using built-in sum."""
        return sum(self.values)

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Adds either all corresponding values of two Simpys or one float to all values of a Simpy."""
        result: Simpy = Simpy([])

        if isinstance(rhs, float):
            for values in self.values:
                result.values.append(values + rhs)
        else:
            i: int = 0
            while i < len(rhs.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1

        return result

    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Raises all values of self to one float power or values of self to corresponding values of rhs."""
        result: Simpy = Simpy([])

        if isinstance(rhs, float):
            for values in self.values:
                result.values.append(values ** rhs)
        else:
            i: int = 0
            while i < len(rhs.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1

        return result

    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Creates a mask based on equality of each value in self to an inputted Simpy's corresponding value or a float."""
        result: list[bool] = []

        if isinstance(rhs, float):
            for values in self.values:
                result.append(values == rhs)
        else:
            i: int = 0
            while i < len(rhs.values):
                result.append(self.values[i] == rhs.values[i])
                i += 1

        return result

    def __gt__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Creates a mask based on whether each value in self is larger than an inputted Simpy's corresponding value or a float."""
        result: list[bool] = []

        if isinstance(rhs, float):
            for values in self.values:
                result.append(values > rhs)
        else:
            i: int = 0
            while i < len(rhs.values):
                result.append(self.values[i] > rhs.values[i])
                i += 1

        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overloads the subscription operator to return the rhs index of self.values, or use an rhs that is a list of bool to return all values corresponding to True."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            result: Simpy = Simpy([])

            for i in range(0, len(self.values)):
                if rhs[i]:
                    result.values.append(self.values[i])

            return result