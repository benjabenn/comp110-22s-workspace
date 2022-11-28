"""Testing some implemented functions to make sure they work in order to help better in office hours."""


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    i: int = 0
    current_max: int = 0
    while i < len(input):
        if i == 0:
            current_max = input[i]
        elif i > 0 and input[i] > current_max:
            current_max = input[i]
        i += 1
    return current_max


def main() -> None:
    list = [1, 8, 9, 3, 6, 11, 4, 2, 1, 4, 2, 7, 5]
    print(f"{max(list)}")


if __name__ == "__main__":
    main()