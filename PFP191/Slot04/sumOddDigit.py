n = int(input("Enter number: "))
sum_odd = 0

while n > 0:
    last_digit = n % 10
    n = n // 10
    if last_digit % 2 != 0:
        print(last_digit)
        sum_odd += last_digit

print(sum_odd)
