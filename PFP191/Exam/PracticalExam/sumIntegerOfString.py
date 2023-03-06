def sumIntegerOfString(string: str) -> int:
    found = "0"
    sign = 1
    result = 0
    for ch in string:
        if ch.isnumeric():
            found += ch
        elif ch == "-":
            sign = -1
        else:
            if sign == -1 and found != "0":
                result += int(found) * -1

                sign = 1
            else:
                result += int(found)
            found = "0"
    return result + int(found)


def main():
    string = input("Enter string: ")
    print(sumIntegerOfString(string))


if __name__ == "__main__":
    main()
