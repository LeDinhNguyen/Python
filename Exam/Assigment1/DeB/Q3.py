'''
Problem 3 (2.5 pts): Write functions to count the
occurence of digit d in the integer n

Inp: n = 13251, d = 1
Out: 2
'''

def countOccurenceDigit(n: int, d: int) -> int:
    '''

    :param n: int - input number
    :param d: int - digit
    :return:
        k is occurence of d in n
    '''
    k = 0
    while n > 0:
        if n % 10 == d:
            k += 1
        n = n // 10

    return k


if __name__ == '__main__':
    n = 13251
    print(countOccurenceDigit(n, 1))
