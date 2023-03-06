def isPrime(number: int) -> bool:
    count = 0
    if number <= 1:
        return 0
    for i in range(2, number // 2):
        if number % i == 0:
            count += 1

    return count == 0


def findSmallestPrimeFromK(k: int) -> int:
    if k <= 1:
        return 2
    else:
        while isPrime(k) == 0:
            k += 1

    return k


num = int(input("Enter number: "))
print(findSmallestPrimeFromK(num))
