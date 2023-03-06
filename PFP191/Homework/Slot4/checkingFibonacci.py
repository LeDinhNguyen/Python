# check Is the number in the Fibonacci sequence
number = int(input("Enter integer: "))
fib1 = 0
fib2 = 1
found = False

while not found:
    if number == fib1:
        print("True")
        found = True
    elif fib1 > number:
        print("False")
        found = True
    else:
        temp = fib1
        fib1 = fib1 + fib2
        fib2 = temp

