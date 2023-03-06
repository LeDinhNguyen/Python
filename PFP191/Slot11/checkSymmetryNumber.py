def addDigit(num: int) -> list:
    num_list = []
    while num > 0:
        num_list.append(num % 10)
        num = num // 10
    return num_list

def checkSymmetryNumber(num: int):
    num_list = addDigit(num)
    i = 0
    j = len(num_list) - 1
    while i < j:
        if num_list[i] == num_list[j]:
            i += 1
            j -= 1
        else:
            return False

    return True

num = 1234567
num1 = 12221
print(checkSymmetryNumber(num))
print(checkSymmetryNumber(num1))
