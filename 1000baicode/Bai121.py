def countDigit(n: int) -> int:
    count = 0
    while n > 0:
        count += 1
        n = n // 10
def isAmstrongNumber(n: int) -> bool:
    count = 0
    k = countDigit(n)
    while n > 0:
        count += (n % 10) ** k

    return n == count

print(isAmstrongNumber())
