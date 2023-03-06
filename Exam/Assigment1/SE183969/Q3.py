'''
Problem 3 (2.5 pts): Write functions to find
the biggest digit in the integer n

Inp: n = 13251
Out: 5
'''

def findBiggestDigit(n: int):
    '''

    :param n: int
    :return: d is biggest digit in the number n
    '''
    d = 0
    while n > 0:
        if d < n % 10:
            d = n % 10
        n = n // 10
    return d


if __name__ == '__main__':
    n = 13251
    print(findBiggestDigit(n))
