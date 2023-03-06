def calSn(n: int):
    s = 1
    for i in range(1, n + 1):
        s += 1
        s = 1 / s
    return s


print(calSn(1))
