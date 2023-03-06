def checkPrimeInteger(num: int) -> bool:
    count = 0
    for i in range(2, num):
        if num % i == 0:
            count += 1
    return count == 0


num = int(input("Enter number: "))
print(checkPrimeInteger(num))
