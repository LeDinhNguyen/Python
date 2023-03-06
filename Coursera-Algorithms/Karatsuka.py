import time


def Karatsuka(x: int, y: int):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    number_length = max(len(str(x)), len(str(y)))
    mid = int(number_length // 2)

    a = x // 10 ** (mid)
    b = x % 10 ** (mid)
    c = y // 10 ** (mid)
    d = y % 10 ** (mid)

    karat_a_c = Karatsuka(a, c)
    karat_b_d = Karatsuka(b, d)
    karat_ac_bd = Karatsuka(a + b, c + d)

    return (
        (karat_a_c * (10 ** (number_length)))
        + ((karat_ac_bd - karat_a_c - karat_b_d) * 10 ** (mid))
        + karat_b_d
    )


a = int(input("a = "))
b = int(input("b = "))

print(Karatsuka(a, b))
print(a * b)
