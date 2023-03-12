def findIntegerOfString(string: str) -> list:
    found = "0"
    sign = 1
    num_list = []

    for ch in string:
        if ch == "-":
            sign = -1
        elif ch.isnumeric():
            if found == "0" and ch == "0":
                num_list.append(int(ch))
            else:
                found += ch
        else:
            cur_num = int(found) * sign
            if cur_num != 0:
                num_list.append(cur_num)

            if sign == -1:
                sign = 1

            found = "0"
    cur_num = int(found) * sign
    if cur_num != 0:
        num_list.append(cur_num)
    print(num_list)
    return num_list


def checkAscending(string: str) -> bool:
    num_list = findIntegerOfString(string)
    pre_num = num_list[0]
    for i in range(1, len(num_list)):
        if num_list[i] >= pre_num:
            pre_num = num_list[i]
        else:
            return False
    return True


def main():
    string = input("Enter the string: ")
    print(checkAscending(string))

if __name__ == "__main__":
    main()
