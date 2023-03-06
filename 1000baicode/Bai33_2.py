def S(n: int):
    s = 0
    for i in range(n):
        s = s + 2
        s = s ** 0.5
    return s


print(S(1))
