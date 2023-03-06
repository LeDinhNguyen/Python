'''

Problem 1 (2.5pts): Write functions to calculate
the value of S(n) as following equation:
S(n) = F(n) / 1! + F(n-1) / 2! + ... + 1/n!
Where F(k) = 1 + 2 + 3 + ... + k

Inp: n = 2
Out: 3.50


'''

def Fn(n: int) -> int:
    if n == 1:
        return 1
    s = 0
    for i in range(1, n+1):
        s += i
    return s

def factorial(n: int) -> int:
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

def calcSn(n: int) -> float:
    result = 0.0
    for i in range(1, n + 1):
        result += (Fn(n + 1 - i)) / factorial(i)
    return result



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = 2
    print("Result = %.2f" % calcSn(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
