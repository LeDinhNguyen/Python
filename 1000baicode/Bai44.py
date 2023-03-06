def sumOfDigitOfInteger(n: int) -> int:
    sum_digit = 0
    while n > 0:
        sum_digit += n % 10
        n = n // 10
    return sum_digit


print(sumOfDigitOfInteger(123456789))
