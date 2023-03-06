number = int(input("Enter number: "))
sum: int = 0

for i in range(1, number + 1):
    sum += number/(number+1)

print(sum)
