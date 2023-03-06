def isPrime(n: int):
    count = 0
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                count += 1
    return count == 0


def findPrimeCommonDivisor(a: int, b: int) -> int:
    div = 0
    for i in range(1, len(min(a, b)) + 1):
        if a % i == 0 and b % i == 0:
            div = i

    return div
