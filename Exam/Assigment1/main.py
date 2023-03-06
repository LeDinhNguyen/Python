def printFigure(h: int):
    for i in range(h,0,-1):
        for j in range(1, h + 1 - i):
            print(" ", end=" ")
        if i % 2 == 1:
            for j in range(1, i+1):
                print(j, end=" ")
            print("")
        else:
            for j in range(i, 0, -1):
                print(j, end=" ")
            print("")

printFigure(5)
