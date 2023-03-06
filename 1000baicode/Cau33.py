def S(n: int):
    if n == 1:
        return 2**0.5
    else:
        return (2 + S(n - 1)) ** 0.5


print(S(1))
