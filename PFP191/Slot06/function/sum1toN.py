def sum1toN(num):
    sum_num = 0
    for i in range(1, num + 1):
        sum_num += 1
    return sum_num


num = int(input("Enter number: "))
print(sum1toN(num))
