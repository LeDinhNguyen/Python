"""
C(k, n) = (k!) / (n - k)!
"""


def factorial(n: int):
    fac = 1
    for i in range(2, n + 1):
        fac = fac * i
    return fac


def C(k: int, n: int) -> int:
    return int(factorial(n) / (factorial(k) * (factorial(n - k))))


def NewtonRule(n: int):
    for i in range(0, n + 1):
        print(C(i, n), end=" ")
    print()


def PascalTriangle(num: int):
    for i in range(0, num):
        NewtonRule(i)


if __name__ == "__main__":
    number = int(input("Enter number = "))
    PascalTriangle(number)
