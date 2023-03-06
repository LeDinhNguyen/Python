def calSn(x: int, n: int) -> float:
    s = 0
    for i in range(1, n + 1):
        s += x
        s = s ** i
        s = s ** 0.5

    return s
