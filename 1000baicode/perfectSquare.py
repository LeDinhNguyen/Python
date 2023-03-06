def perfectSquare(n: int):
    sqrt_n = int(n**0.5)
    return sqrt_n**2 == n


number = int(input("Enter num = "))
print(perfectSquare(number))
