def printEmptyIsoscelesTriangle(n: int):
    for i in range(n - 1):
        print("  ", end="")
    print("* ", end="")
    for i in range(n - 1):
        print("  ", end="")
    print()

    for i in range(1, n - 1):
        for j in range(n - i - 1):
            print("  ", end="")
        print("* ", end="")
        for j in range(2*i - 1):
            print("  ", end="")
        print("* ", end="")
        for j in range(n-i-1):
            print("  ", end="")
        print("")
    for i in range(2*n - 1):
        print("* ", end="")
    print("")


def printFullIsoscelesTriangle(n: int):
    for i in range(1, n + 1):
        for j in range(n-i):
            print("  ", end="")
        for j in range(2*i-1):
            print("* ", end="")
        for j in range(n-i):
            print("  ", end="")
        print("")


def printFullRightTriangle(n: int):
    for i in range(1, n+1):
        for j in range(i):
            print("* ", end="")
        print("")


def printEmptyRightTriangle(n: int):
    print("* ")
    for i in range(n - 2):
        print("* ", end="")
        for j in range(i):
            print("  ", end="")
        print("* ")
    for i in range(n):
        print("* ", end="")
    print("")


printFullIsoscelesTriangle(5)
print("--"*(2*5-1))
printEmptyIsoscelesTriangle(5)
print("--"*(2*5-1))
printFullRightTriangle(5)
print("--"*(2*5-1))
printEmptyRightTriangle(5)
