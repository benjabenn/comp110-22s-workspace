"""Challenge Question #1; This method was an imitation of the illogical example,
but made logical, a different method of nesting is used in the video"""

choice: int = int(input("Enter a number: "))

if choice < 50:
    if choice < 25:
        print("A")
    else:
        print("B")
else:
    if choice > 75:
        print("C")
    else:
        print("D")