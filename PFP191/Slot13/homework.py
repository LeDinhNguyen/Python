def Bai1(s1: str, s2: str) -> str:
    m = (len(s1) - 1) // 2
    start = s1[0:m+1]
    end = s1[m + 1::]

    return start + s2 + end

def Bai2(string: str) -> str:
    lower_string = ""
    upper_string = ""
    for s in string:
        if s.islower():
            lower_string += s
        if s.isupper():
            upper_string += s


    return lower_string + upper_string

print(Bai1("abcde", "12"))
print(Bai2("pytHonIDE"))