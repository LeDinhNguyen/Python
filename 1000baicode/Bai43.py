def countDigitsOfInteger(n: int) -> int:
    count = 0
    while n > 0:
        count += 1
        n = n // 10

    return count


print(countDigitsOfInteger(12345))
