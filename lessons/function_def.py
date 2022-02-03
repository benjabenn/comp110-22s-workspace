"""An example function definition."""


# Line 4 is a Signature line "contract", line 5 is the docstring, lines 6-9 (nice) are the body block 
def my_max(a: int, b: int) -> int:
    """Returns the largest argument."""
    if a >= b:
        return a
    else:
        return b


# Line 16 is my return address
x: int = 7
y: int = 6
z: int = my_max(x, y)
print(z)
