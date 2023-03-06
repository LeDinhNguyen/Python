n = int(input("Enter number: "))
count = 0 # hieu ung le

for i in range(1, n + 1):
    if (n % i == 0):
        print(i)
        count += 1
print("The number of divisors: ", count)