def findMaximum(a: int, b: int, c: int) -> int:
    maximum = a
    if b < maximum and c < maximum:
        return maximum
    else:
        if b < c:
            maximum = c
        else:
            maximum = b

    return maximum


print(findMaximum(1, 4, 3))
