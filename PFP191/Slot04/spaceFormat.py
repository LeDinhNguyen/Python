number = int(input("Enter number: "))

for i in range(1, number + 1):
    for space in range(number - i):
        print(" ", end=" ")
    for j in range(i):
        print(j + 1, end=" ")
    print("\n")