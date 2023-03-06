def getNonzeroDigit(string: str) -> str:
    digit = ""
    for s in string:
        if s.isdigit() and s != "0":
            digit += s

    if digit == "":
        return str(-1)

    return digit

print(getNonzeroDigit("hfdsbkbfhsd000001sdfsds234"))
