num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

n = min(num1, num2)
gcd = 1


# for
for i in range(1, n + 1):
    if (num1 % i == 0) and (num2 % i == 0):
        gcd = i
print(gcd)

# while
i = 1
gcd = 0
while (i <= num1) and (i <= num2):
    if (num1 % i == 0) and (num2 % i == 0):
        gcd = i
    i += 1
print(gcd)