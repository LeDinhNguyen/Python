def checkIncrease(num_list: list):
    if len(num_list) == 1:
        return 1
    pre_num = num_list[0]
    for i in range(1, len(num_list)):
        if pre_num >= num_list[i]:
            return False
        pre_num = num_list[i]
    return True


num_list = [1, 2, 3, 4, 5, 6, 7, 7]
print(checkIncrease(num_list))
