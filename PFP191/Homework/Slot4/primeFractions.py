number = int(input("Enter number: "))
count = 0

while number % 2 == 0:
    count += 1
    number = int(number / 2)

print(2, count)
count = 0

for i in range(3, number + 1, 2):
    while number % i == 0:
        count += 1
        number = int(number / i)

    if count != 0:
        print(i, count)
