def isPrime(number: int):
    count = 0
    for i in range(2, number):
        if number % i == 0:
            count += 1
    return count == 0


num = int(input("Enter number: "))
prime = num + 1
while not isPrime(prime):
    prime += 1

print(prime)
