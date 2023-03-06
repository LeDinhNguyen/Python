def integerOfString(string: str) -> str:
    number_string = ""
    for s in string:
        if s.isnumeric():
            number_string += s

    return number_string

print(integerOfString("I am 25 years and 10 moths old"))
