def countNumberOfDigit(number: int) -> int:
    count = 0
    while number > 0:
        number = number // 10
        count += 1
    return count


def countAppearanceOfDgit(number: int, digit: int) -> int:
    count = 0
    for i in range(1, number + 1):
        lastDigit = number % 10
        number = number // 10
        if lastDigit == digit:
            count += 1
    return count


def findMajority(number: int) -> int:
    numberOfDigit = countNumberOfDigit(number)
    for digit in range(0, 10):
        if countAppearanceOfDgit(number, digit) > (numberOfDigit/2):
            return digit

    return -1

print(findMajority(1234))
