"""Some examples of tender, loving functions."""


def love(name: str) -> str:
    """Given a name as a parameter, returns a loving string."""
    return f"I love you {name}!"


def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loving message n times."""
    love_note: str = ""
    i: int = 0
    while i < n:
        love_note += love(to) + "\n"
        i += 1
    return love_note


# loved_people: str = input("Who do you love? ")
# number: int = int(input("How many times? "))
# print(spread_love(loved_people, number))