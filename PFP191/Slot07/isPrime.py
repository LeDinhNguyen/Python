def isPrime(number: int) -> bool:
    count = 0
    if number <= 1:
        return 0
    for i in range(2, number // 2):
        if number % i == 0:
            count += 1

    return count == 0


num = int(input("Enter number: "))
print(isPrime(num))
