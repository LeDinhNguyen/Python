'''

Problem 1 (2.5pts): Write functions to calculate
the value of S(n) as following equation:
S(n) = 1 + 1/2! + 1/3! + ... + 1/n!

Inp: n = 2
Out: 1.5

'''


def calcSn(n: int) -> float:
    result = 0.0
    for i in range(1, n+1):
        result += 1/i


    return result



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = 2
    print("Result = %.2f" % calcSn(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
