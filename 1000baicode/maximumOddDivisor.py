def maximumOddDivisor(n: int) -> int:
    max_div = 0
    for i in range(2, n // 2):
        if n % i == 0 and i % 2 != 0:
            max_div = i
    return max_div


print(maximumOddDivisor(100))
