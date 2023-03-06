def printFullRecangle(m: int, n: int):
    for i in range(n):
        for j in range(m):
            print("* ", end="")
        print("")

def printIsoscelesRecangle(m: int, n: int):
    for i in range(m):
        print("* ", end="")
    print("")

    for i in range(n - 2):
        print("* ", end= "")
        for j in range(m - 2):
            print("  ", end="")
        print("* ")

    for i in range(m):
        print("* ", end="")
    print("")        

printFullRecangle(7, 4)
print("- " * 7)
printIsoscelesRecangle(7, 4)
