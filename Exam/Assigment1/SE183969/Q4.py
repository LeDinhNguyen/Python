'''
Problem 4:
A temporary prime number is a positive integer whose
all divisors (except 1 and its value) are prime number.
A prime number is also the temporary prime number
The first temporary prime number is 2.

Write a function to print all temporary prime
number that is smaller than or equal to n.

For example,
6 is a temporary prime number cuz
its divisors are 2, 3 (prime number)

Inp: 10
Out: 2 3 4 5 6 7 9 10

'''

def isPrime(n: int) -> bool:
    count = 0
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                count += 1
    return count == 0

def checkTemporaryPrime(n: int) -> int:
    '''

    :param n: int
    :return:
        1 - if n is temporary prime number
        0 - if n is not temporary prime number
    '''
    prime_divisors = 0
    all_divisors = 0
    for i in range(2, n):
        if n % i == 0:
            all_divisors += 1
            if isPrime(i):
                prime_divisors += 1
    if prime_divisors == all_divisors:
        return 1
    else:
        return 0


def printAllTemporaryNumber(n: int):
    '''

    :param n: int
    :return: no return
    :task: print all temporary number in [2, n]
    '''
    for i in range(2, n + 1):
        if checkTemporaryPrime(i):
            print(i, end=" ")




if __name__ == '__main__':
    n = 10
    printAllTemporaryNumber(n)
