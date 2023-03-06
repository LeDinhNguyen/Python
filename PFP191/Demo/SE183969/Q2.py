'''
Problem 2 (2.5 pts): Write functions to print the
following figure with the height of h

Inp: h = 5
Out:
*
**
***
****
*****
'''

def printFigure(h: int):
    for i in range(1, h+1):
        for j in range(i):
            print("*", end="")
        print("")

    return


if __name__ == '__main__':
    n = 5
    printFigure(n)
