'''
Problem 2 (2.5 pts): Write functions to print the
following figure with the height of h

Inp: h = 5
Out:
        1
      2 1
    1 2 3
  4 3 2 1
1 2 3 4 5
'''

def printFigure(h: int):
    for i in range(1, n + 1):
        for j in range(n -i):
            print("  ", end="")
        if i % 2 == 1:
            for j in range(i):
                print(j + 1, end = " ")
            print("")
        else:
            for j in range(i, 0, -1):
                print(j, end=" ")
            print("")
    return


if __name__ == '__main__':
    n = 5
    printFigure(n)
