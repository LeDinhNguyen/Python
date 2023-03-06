def calSn(n: int) -> float:
    s = 0
    for i in range(1, n + 1):
        s += i
        s = s ** 0.5
    return s


print(calSn(3))
