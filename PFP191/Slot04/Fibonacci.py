number = int(input("Enter number: "))
fib1 = 0
fib2 = 1

if number == 1:
    print(0)
elif number == 2:
    print(0, 1)

for i in range(1, number + 1):
    print(fib1, end=" ")

    # swap number
    temp = fib1
    fib1 = fib1 + fib2
    fib2 = temp


