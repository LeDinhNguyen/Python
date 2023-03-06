number = int(input("Enter number: "))

for i in range(0, number + 1):
    for j in range(1, number + 1 - i):
        print(number + 1 - i - j, end=" ")
    print("\n")


