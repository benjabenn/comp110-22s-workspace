"""Testing some implemented functions to make sure they work in order to help better in office hours."""


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    i: int = 0
    current_max: int = 0
    while i < len(input):
        if i == 0:
            current_max = input[i]
        elif i > 0:
            if input[i] > current_max:
                current_max = input[i]
        i += 1
    return current_max


def main() -> None:
    list = [10, 4, 5, 8, 7, 9]
    print(f"{max(list)}")


if __name__ == "__main__":
    main()