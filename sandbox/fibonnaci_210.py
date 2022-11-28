"""Testing Lecture 5's recursive fibonacci program"""


def fib(n: int) -> int:
    # print("fib(n), n=", n)
    if n == 0:
        return 0
    else:
        if n == 1:
            return 1
        else:
            return (fib(n - 1) + fib(n - 2))


def main() -> None:
    n = 1000
    i = 0
    while i < n:
        print(fib(i))
        i += 1


if __name__ == "__main__":
    main()