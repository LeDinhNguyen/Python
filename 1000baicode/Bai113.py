def fact(n: int) -> int:
    f = 1
    for i in range(1, n+1):
        f *= i
    return f


def sin(x: int) -> float:
    s = 0
    for i in range(x):
        s += (-1)**i * (x**(2*i+1))/fact(2*i+1)

    return s


print(sin(1))
