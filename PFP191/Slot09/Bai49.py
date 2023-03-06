def findFirstDigitOfInteger(n: int) -> int:
    firstDigit = 0
    while n >= 10:
        n = n // 10

    return n


print(findFirstDigitOfInteger(232314))
