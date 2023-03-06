def findIntegerOfString(string: str):
    found = "0"
    sign = 1
    num_list = []

    for ch in string:
        if ch == "-":
            sign = -1
        elif ch.isnumeric():
            found += ch
        else:
            cur_num = int(found) * sign
            num_list.append(cur_num)

            if sign == -1:
                sign = 1

            found = "0"
    return num_list


def checkAscending(string: str) -> bool:
    num_list = findIntegerOfString(string)
    pre_num = num_list[0]
    flag = 0
    while flag == 0:
        for i in range(1, len(num_list)):
            if num_list[i] > pre_num:
                flag += 1
    return flag != 0


def main():
    print(checkAscending("-12d-1njda-3"))


if __name__ == "__main__":
    main()
